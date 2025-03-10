import time
import threading
import random
import asyncio
import websockets
import json
import tkinter as tk
from threading import Thread
from tkinter import scrolledtext

def decay_needs():
    while True:
        time.sleep(90)
        pet["hunger"] -= 5
        pet["happiness"] -= 3

        pet["hunger"] = max(0, pet["hunger"])
        pet["happiness"] = max(0, pet["happiness"])

def get_mood():
    if pet["happiness"] < 30 and pet["hunger"] < 30:
        return "Miserable 😭"
    elif pet["hunger"] < 30:
        return "Hungry 🤤"
    elif pet["happiness"] < 30:
        return "Sad 😔"
    return "Content 😊"
money = 50


while True:
    print("----------------------")
    print("WELCOME TO CAB'S PET WORLD! CHOOSE YOUR PET.")
    print("----------------------")
    print("1. Dog 🐶")
    print("2. Cat 🐈")
    print("3. Fish 🐟")
    print("4. Bird 🐦")
    print("----------------------")

    pet_options = {
        "1": "Dog",
        "2": "Cat",
        "3": "Fish",
        "4": "Bird"
    }

    petchoice = input("> ")

    if petchoice in pet_options:
        pet_type = pet_options[petchoice]
        print("----------------------")
        print(f"Are you sure you want to pick {pet_type} as your pet?")
        print("----------------------")
        petchoiceyn = input("> Y/N? ").strip().upper()
        if petchoiceyn == "Y":
            print("----------------------")
            print(f"You have chosen {pet_type} as your pet.")
            print("----------------------")
            break
        if petchoiceyn == "N":
            print("...")
            continue
        else:
            print("----------------------")
            print("Invalid input, pick Y or N.")
            print("----------------------")
    else:
        print("----------------------")
        print("Invalid input, pick a number between 1 and 4.")
        print("----------------------")

while True:
    print("----------------------")
    print("NAME YOUR PET")
    print("----------------------")
    print(f"What will you name your {pet_type}?")
    print("----------------------")
    pet_name = input("> ")
    if len(pet_name) > 0:
        print("----------------------")
        print(f"Do you want to name your {pet_type} {pet_name}?")
        print("----------------------")
        choicename = input("> Y/N? ").strip().upper()
        if choicename == "Y":
            print("----------------------")
            print(f"Your {pet_type} has successfully been named {pet_name}!")
            print("----------------------")
            break
        if choicename == "N":
            print("...")
            continue
        else:
            print("----------------------")
            print("Invalid input, pick Y or N.")
            print("----------------------")
    else:
        print("----------------------")
        print("Name cannot be empty!")
        print("----------------------")
pet = {
    "type": pet_type,
    "name": pet_name,
    "hunger": 100,
    "happiness": 100
}

needs_thread = threading.Thread(target=decay_needs, daemon=True)
needs_thread.start()
inventory = []
while True:
    print("----------------------")
    print("MAIN MENU")
    print("----------------------")
    print(f"1. Play with {pet_name} ⚽")
    print(f"2. Feed {pet_name} 🦴")
    print(f"3. {pet_name}'s Stats ❓")
    print("4. Inventory 📦")
    print("5. Store 🏪")
    print("6. Work 💼")
    print("7. Pet Hatching Center 🥚")
    print("8. Global Chat 💬")
    print("----------------------")
    hubchoice = input("> ")
    if hubchoice == "1":  # Play with pet
        if "Rubber Ball" in inventory:
            inventory.remove("Rubber Ball")  # Consume Rubber Ball
            pet["happiness"] = min(100, pet["happiness"] + 15)  # Increase happiness (max 100)
            print("----------------------")
            print(f"You played with {pet_name}! Happiness increased! 😊")
            print("Used 1 Rubber Ball 🎾")
            print("----------------------")
        else:
            print("----------------------")
            print(f"You don't have a Rubber Ball! Buy one from the store. 🏪")
            print("----------------------")

    elif hubchoice == "2":  # Feed pet
        if "Pet Kibble" in inventory:
            inventory.remove("Pet Kibble")  # Consume Pet Kibble
            pet["hunger"] = min(100, pet["hunger"] + 20)  # Increase hunger (max 100)
            print("----------------------")
            print(f"You fed {pet_name}! Hunger increased! 🍖")
            print("Used 1 Pet Kibble 🦴")
            print("----------------------")
        else:
            print("----------------------")
            print(f"You don't have Pet Kibble! Buy some from the store. 🏪")
            print("----------------------")
    elif hubchoice == "3":
        print("----------------------")
        print(f"{pet_name}'s STATS")
        print("----------------------")
        print(f"Species: {pet_type}")
        print(f"Hunger: {pet['hunger']}")
        print(f"Happiness: {pet['happiness']}")
        print("Overall Mood:", get_mood())
        print("0. Exit")
        print("----------------------")
        statuschoice = input("> ")
        if statuschoice == "0":
            continue
    elif hubchoice == "4":
        print("----------------------")
        print("INVENTORY")
        print("----------------------")
        if inventory:
            item_counts = {}
            for item in inventory:
                item_counts[item] = item_counts.get(item, 0) + 1
            for item, count in item_counts.items():
                print(f"- {item} x{count}")
        else:
            print("No Items Found!")
        print("0. Exit")
        print("----------------------")

        invchoice = input("> ")
        if invchoice == "0":
            continue

    elif hubchoice == "5":
        while True:
            print("----------------------")
            print("STORE")
            print(f"Your Money: ${money} 💸")
            print("----------------------")
            print("Items for Sale")
            print("1. Pet Kibble $10 🦴")
            print("2. Rubber Ball $10 ⚽")
            print("0. Exit")
            print("----------------------")
            strchoice = input("> ")

            store_items = {
                "1": {"name": "Pet Kibble", "price": 10},
                "2": {"name": "Rubber Ball", "price": 10},
            }

            if strchoice == "0":
                break  # Exit store menu

            if strchoice in store_items:
                item = store_items[strchoice]
                if money >= item["price"]:
                    money -= item["price"]
                    inventory.append(item["name"])  # Add to inventory
                    print(f"You purchased {item['name']}! It has been added to your inventory.")
                else:
                    print("Not enough money to buy this item!")
            else:
                print("Invalid choice, please try again.")

        # Global variable for money

    # Define Fishing Game Function
    def fishing_game():
        adjectives = {
            "Tiny": 3, "Common": 4, "Shiny": 5, "Golden": 7, "Legendary": 10
        }
        fish_types = {
            "Trout": 3, "Salmon": 4, "Bass": 5, "Tuna": 7, "Shark": 10
        }

        print("🎣 You cast your line and wait...")
        
        # Random wait time with dots appearing over time
        wait_time = random.uniform(2, 5)
        start_wait = time.time()
        
        while time.time() - start_wait < wait_time:
            print(". ", end="", flush=True)
            time.sleep(random.uniform(0.5, 1.2))
        
        print("\n🎯 A fish is biting! Type 'C' to catch it!")

        start_time = time.time()
        catch_input = input("> ").strip().upper()
        reaction_time = time.time() - start_time

        if catch_input == "C" and 0.1 < reaction_time < 0.5:  # Success window
            adjective = random.choices(list(adjectives.keys()), weights=[40, 30, 20, 8, 2])[0]
            fish_type = random.choices(list(fish_types.keys()), weights=[40, 30, 20, 8, 2])[0]
            fish_value = min(adjectives[adjective] + fish_types[fish_type], 35)

            print(f"✅ You caught a {adjective} {fish_type} and earned ${fish_value}!  Total Money: ${money}")
            return fish_value
        else:
            print("❌ The fish got away!")
            return 0

    # Define Word Factory Function
    def wordfac():
        global money  # Ensure money is modified globally
        word_bank = {
            "easy": ["cat", "dog", "fish", "hat", "tree", "sun", "ball", "cup", "lamp", "frog"],
            "medium": ["guitar", "window", "banana", "purple", "rocket", "castle", "tunnel", "parrot", "blanket", "furnace"],
            "hard": ["elephant", "umbrella", "pineapple", "chocolate", "notebook", "laboratory", "microscope", "tournament", "watermelon", "adventure"]
        }
        time_limits = {"easy": 5, "medium": 4, "hard": 3}  # Time limits per difficulty
        
        while True:
            print("----------------------")
            print("WORD FACTORY 🏭")
            print("Choose difficulty:")
            print("1. Easy (3-5 letters)")
            print("2. Medium (6-8 letters)")
            print("3. Hard (9+ letters, bonus pay)")
            print("0. Exit to Work Menu")
            print("----------------------")
            diffchoice = input("> ")

            if diffchoice == "0":
                return  # Exit only to Work Menu
            
            diffmap = {"1": "easy", "2": "medium", "3": "hard"}
            if diffchoice not in diffmap:
                print("Invalid choice, try again.")
                continue

            diff = diffmap[diffchoice]
            word = random.choice(word_bank[diff])
            time_limit = time_limits[diff]  # Get the corresponding time limit

            print(f"TYPE WORD: {word.upper()} (You have {time_limit} seconds!)")
            start_time = time.time()
            wordfacin = input("> ").strip()
            elapsed_time = time.time() - start_time

            if elapsed_time > time_limit:
                print("⏳ Too slow! You ran out of time!")
            elif wordfacin.lower() == word.lower():
                wordlen = len(word)
                earnings = wordlen
                if diff == "hard":
                    earnings *= 2  # Double pay for hard mode
                money += earnings
                print(f"✅ Correct! You earned ${earnings}. Total Money: ${money}")
            else:
                print("❌ Incorrect! No earnings.")

    # Work Menu Logic
    def work_menu():
        global money  # Ensure we modify money globally
        while True:
            print("----------------------")
            print("WORK")
            print("----------------------")
            print("1. Word Factory 🏭")
            print("2. Fishing 🎣")
            print("0. Exit")
            print("----------------------")
            workchoice = input("> ").strip()

            if workchoice == "1":
                wordfac()  # Play Word Factory and return to work menu
            elif workchoice == "2":
                earnings = fishing_game()
                money += earnings  # Add earnings from fishing
            elif workchoice == "0":
                return  # Properly exit the work menu
            else:
                print("Invalid choice, try again.")

# Main Game Hub

    if hubchoice == "6":
        work_menu()
    egg_data = {
    "1": {  # Basic Egg
        "cost": 100,
        "pets": {
            "Common": ["Dog", "Cat", "Rabbit"],
            "Uncommon": ["Fox", "Parrot"],
            "Rare": ["Wolf", "Eagle"],
            "Epic": ["Phoenix"],
            "Mythic": ["Baby Dragon"]
        },
        "weights": [50, 30, 15, 4, 1]  # Probability distribution
    },
    "2": {  # Golden Egg
        "cost": 500,
        "pets": {
            "Common": ["Fox", "Parrot"],
            "Uncommon": ["Wolf", "Eagle"],
            "Rare": ["Phoenix", "Griffin"],
            "Epic": ["Hydra"],
            "Mythic": ["Dragon"]
        },
        "weights": [30, 30, 20, 15, 5]
    },
    "3": {  # Diamond Egg
        "cost": 1000,
        "pets": {
            "Common": ["Wolf", "Eagle"],
            "Uncommon": ["Phoenix", "Griffin"],
            "Rare": ["Hydra", "Cerberus"],
            "Epic": ["Titan", "Pegasus"],
            "Mythic": ["Ancient Dragon"]
        },
        "weights": [20, 25, 25, 20, 10]
    }
}

# Function must be defined BEFORE calling it
    def hatch_egg():
        global money, pet_name, pet_type  # Use global money and pet dictionary

        print("----------------------")
        print("PET HATCHING CENTER")
        print("----------------------")
        print("1. Basic Egg $100 🥚")
        print("2. Golden Egg $500 🥇")
        print("3. Diamond Egg $1000 💎")
        print("0. Exit")
        print("----------------------")

        hatchchoice = input("> ").strip()

        if hatchchoice == "0":
            return  # Exit

        if hatchchoice in egg_data:
            egg = egg_data[hatchchoice]
            if money < egg["cost"]:
                print("Not enough money!")
                return

            money -= egg["cost"]  # Deduct money

            # Select pet rarity based on weights
            rarities = list(egg["pets"].keys())
            chosen_rarity = random.choices(rarities, weights=egg["weights"], k=1)[0]
            pet_species = random.choice(egg["pets"][chosen_rarity])

            # Hatching animation
            print("\nHatching...")
            roulette = ["🐣", "🥚", "💫", "✨", "🎇", "🎆"]
            for _ in range(10):  # Simulate spinning effect
                print(random.choice(roulette), end="\r", flush=True)
                time.sleep(0.2)

            # Final reveal
            print(f"\n🎉 You hatched a {chosen_rarity.upper()}: {pet_species}! 🎉\n")
            
            # Ask if player wants to replace their current pet
            print("Do you want to replace your current pet? (Y/N)")
            choice = input("> ").strip().lower()  # Get input once

            if choice == "y":
                while True:
                    print("Name your new pet:")
                    new_name = input("> ").strip()
                    if new_name:
                        pet_name = new_name
                        pet_type = pet_species
                        break
                    pet = {
                        "type": pet_type,
                        "name": pet_name,
                        "hunger": 100,
                        "happiness": 100
                    }
                    print(f"Your new pet is {pet['name']} the {pet_species}! 🏡")
            elif choice == "n":
                print("You kept your current pet.")
            else:
                print("Invalid choice!")


    if hubchoice == "7":
        hatch_egg()  # ✅ Now this works because hatch_egg is already defined

    class ChatClient:
        def __init__(self, root):
            self.root = root
            self.root.title("Global Chat")

            self.text_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=20, width=50)
            self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            self.entry = tk.Entry(root, width=50)
            self.entry.pack(padx=10, pady=5, fill=tk.X)
            self.entry.bind("<Return>", self.send_message)

            self.send_button = tk.Button(root, text="Send", command=self.send_message)
            self.send_button.pack(pady=5)

            self.username = None
            self.websocket = None
            self.running = True  # Track if chat is running

            self.loop = asyncio.new_event_loop()  # Create a new event loop
            self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        def start_websocket_thread(self):
            """Starts the WebSocket connection in a separate thread."""
            thread = Thread(target=self.run_websocket, daemon=True)
            thread.start()

        def run_websocket(self):
            """Runs the WebSocket connection in a separate event loop."""
            asyncio.set_event_loop(self.loop)  # Set the event loop for this thread
            self.loop.run_until_complete(self.connect())

        async def connect(self):
            """Handles WebSocket connection and message reception."""
            try:
                self.websocket = await websockets.connect("ws://localhost:8000/ws")
                self.username = input("Enter your username: ")

                # Send join message
                await self.websocket.send(json.dumps({"username": self.username, "message": "HAS ENTERED THE CHAT"}))

                # Start receiving messages
                while self.running:
                    response = await self.websocket.recv()
                    self.loop.call_soon_threadsafe(self.root.after, 0, self.display_message, response)
            except Exception as e:
                self.loop.call_soon_threadsafe(self.root.after, 0, self.display_message, f"Connection error: {e}")
                
        def display_message(self, message):
            """Displays a message in the chat window."""
            self.text_area.config(state=tk.NORMAL)
            self.text_area.insert(tk.END, message + "\n")
            self.text_area.config(state=tk.DISABLED)
            self.text_area.yview(tk.END)

        def send_message(self, event=None):
            """Handles sending messages to the server."""
            message = self.entry.get()
            self.entry.delete(0, tk.END)

            if message:
                self.loop.call_soon_threadsafe(asyncio.create_task, self._send_message_async(message))

        async def _send_message_async(self, message):
            """Sends a message asynchronously."""
            if self.websocket:
                await self.websocket.send(json.dumps({"username": self.username, "message": message}))

        def on_close(self):
            """Handles cleanup when the chat window is closed and returns to main menu."""
            self.running = False
            if self.websocket:
                self.loop.call_soon_threadsafe(asyncio.create_task, self.websocket.send(
                    json.dumps({"username": self.username, "message": "HAS LEFT THE CHAT"})
                ))
                self.loop.call_soon_threadsafe(asyncio.create_task, self.websocket.close())

            self.root.quit()  # Stop the Tkinter event loop
            self.root.destroy()  # Close the window


    def open_chat():
        """Opens the chat interface and ensures it returns to the main menu when closed."""
        root = tk.Tk()
        client = ChatClient(root)

        # Start WebSocket in a separate thread
        client.start_websocket_thread()

        root.mainloop()  # Wait for chat window to close
        print("\nReturning to MAIN MENU...\n")  # Debugging statement

    if hubchoice == "8":
        print("Opening chat...")  # Debugging statement
        open_chat()  # Run chat
        continue  # Return to the main menu when chat closes
