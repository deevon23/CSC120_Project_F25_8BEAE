game_name = "Turbo"
print(f"Welcome to {game_name}!")
print("=================")

# Ask for the character's name
name = input("Before we begin, what is your character's name?\n> ")

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

# Build a dictionary called "player"
player = {"name": name, "health": 100, "coin": 0}

# Build a list called "events"
events = ["find a coin", "meet a monster", "do nothing"]

# complete this line to randomly choose one event from the list `events`
import random
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player["coin"] += 1
    print(f"{player["name"]} found a coin, {player["name"]} now has {player["coin"]} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{player["name"]} got hurt during the combat with monster, health is now {player["health"]}.")
elif event == "do nothing":
    pass