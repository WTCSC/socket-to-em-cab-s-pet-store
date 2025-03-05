---

# Cab's Pet World

Welcome to **Cab's Pet World**, a virtual pet simulation game where you can adopt, name, take care of, and play with a variety of pets. This game also features mini-games, such as **Word Factory** and **Fishing**, to earn money and buy items to enhance your pet experience. The game includes a dynamic **needs decay system**, where your pet's hunger and happiness decay over time, and multiplayer features for global chat and pet trading.

---

## Features

- **Pet Care**: Choose from multiple pets (Dog, Cat, Fish, Bird) and take care of them by feeding them or playing with them to keep their stats in check.
- **Needs Decay**: Your pet's hunger and happiness decay over time, even when you are offline, encouraging you to check in regularly.
- **Mini-Games**: 
  - **Word Factory**: Type words correctly to earn money.
  - **Fishing**: Catch fish to earn money.
- **Pet Hatching**: Hatch eggs of varying rarity to get unique pets like dragons or phoenixes.
- **Store**: Purchase items (e.g., Pet Kibble, Rubber Balls) to care for your pet.
- **Global Chat**: Chat with other players in real-time using WebSocket.

---

## Getting Started

To play the game, you will need to have **Python** installed. This game is designed to run in a console-based environment and uses **Tkinter** for the GUI and **WebSockets** for real-time chat functionality.

### Prerequisites

Make sure you have the following Python libraries installed:

- **asyncio**
- **websockets**
- **tkinter**
- **random**
- **time**
- **json**
- **threading**

You can install the necessary libraries using:

```bash
pip install websockets
```

**Note**: Tkinter is typically included with Python. If not, you'll need to install it based on your system.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cabs-pet-world.git
```

2. Navigate to the project directory:

```bash
cd cabs-pet-world
```

3. Run the game:

```bash
python pet_game.py
```

---

## How to Play

1. **Choose Your Pet**: The game will prompt you to choose a pet (Dog, Cat, Fish, or Bird).
2. **Name Your Pet**: After choosing a pet, you can give it a name.
3. **Care for Your Pet**: Use the **Main Menu** to interact with your pet, including feeding, playing, checking stats, and more.
4. **Mini-Games**: Earn money through the **Word Factory** or **Fishing** mini-games to buy items from the store or hatch new pets.
5. **Chat**: You can chat with other players using the integrated global chat.

---

## Key Commands

- **Main Menu**:
  - `1`: Play with your pet
  - `2`: Feed your pet
  - `3`: Check pet stats
  - `4`: Check your inventory
  - `5`: Visit the store
  - `6`: Work (e.g., Word Factory, Fishing)
  - `7`: Hatch a pet egg
  - `8`: Chat with other players

- **Store**: Buy items for your pet using your in-game currency.

- **Global Chat**: Enter your username and send messages to interact with other players.

---

### Architecture

- **Server-Client Model**: The game utilizes WebSockets for multiplayer communication and a basic client-server architecture.
- **Threads**: A background thread handles the decay of pet needs (hunger, happiness).
- **Tkinter GUI**: The **global chat** is built with **Tkinter**, providing a simple interface for sending and receiving messages.

### Code Structure

- `pet_game.py`: The main game script containing all the logic for pet management, mini-games, and store interactions.
- `server.py`: The server manager for the game.
- `client.py`: The client manager for the game.
---

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes. If you encounter any issues or have feature requests, please open an issue.

---

## License

This project is open source and available under the MIT License.

---

Enjoy playing **Cab's Pet World**, and may your pet thrive in this virtual world! 🎮🐾

---