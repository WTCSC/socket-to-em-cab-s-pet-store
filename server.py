import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# Store connected clients
connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handles WebSocket connections."""
    await websocket.accept()
    connected_clients.add(websocket)
    
    # Notify all users that someone joined
    join_message = json.dumps({"username": "SERVER", "message": "A user has joined the chat."})
    await broadcast(join_message)

    try:
        while True:
            message = await websocket.receive_text()
            
            # Parse JSON message
            try:
                data = json.loads(message)
                username = data.get("username", "Unknown")
                text = data.get("message", "")

                # Limit message size
                if len(text) > 500:
                    continue  # Ignore very long messages
                
                # Broadcast message
                broadcast_message = json.dumps({"username": username, "message": text})
                await broadcast(broadcast_message)

            except json.JSONDecodeError:
                print("Error: Received non-JSON message")

    except WebSocketDisconnect:
        connected_clients.discard(websocket)  # Use discard to avoid KeyError

        # Notify all users that someone left
        leave_message = json.dumps({"username": "SERVER", "message": "A user has left the chat."})
        await broadcast(leave_message)

async def broadcast(message):
    """Send message to all connected clients."""
    for client in connected_clients:
        try:
            await client.send_text(message)
        except Exception:
            connected_clients.discard(client)  # Remove disconnected clients

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
