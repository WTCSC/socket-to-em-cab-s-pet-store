import asyncio
import json
import websockets
import tkinter as tk
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.window = tk.Tk()
        self.window.title("Global Chat")
        self.window.geometry("400x400")

        self.chat_display = scrolledtext.ScrolledText(self.window, state='disabled')
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(self.window)
        self.message_entry.pack(padx=10, pady=5, fill=tk.X)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.websocket = None
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle closing the window

        asyncio.create_task(self.connect())  # Start the WebSocket connection

    async def connect(self):
        """Establish and maintain a WebSocket connection."""
        try:
            self.websocket = await websockets.connect("ws://localhost:8000/ws")
            await self.send_chat_message(f"{self.username} has joined the chat!")
            await self.receive_chat_messages()
        except Exception as e:
            print(f"Connection error: {e}")

    async def send_chat_message(self, message):
        """Send a chat message to the server."""
        if self.websocket:
            data = json.dumps({"username": self.username, "message": message})
            await self.websocket.send(data)

    def send_message(self):
        """Send a message when the Send button is clicked."""
        message = self.message_entry.get()
        if message:
            asyncio.create_task(self.send_chat_message(message))
            self.message_entry.delete(0, tk.END)

    async def receive_chat_messages(self):
        """Listen for messages from the server and update the chat display."""
        try:
            async for response in self.websocket:
                self.chat_display.configure(state='normal')
                self.chat_display.insert(tk.END, f"{response}\n")
                self.chat_display.configure(state='disabled')
                self.chat_display.yview(tk.END)
        except websockets.exceptions.ConnectionClosed:
            print("Server disconnected")

    def on_close(self):
        """Handle the window closing event."""
        if self.websocket:
            asyncio.create_task(self.websocket.close())
        self.window.destroy()

def start_global_chat(username):
    client = ChatClient(username)
    asyncio.run(client.window.mainloop())  # Properly run Tkinter with asyncio
