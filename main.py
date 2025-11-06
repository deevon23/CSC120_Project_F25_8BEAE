

import random

# Game name
game_name = "Turbo"
print(f"Welcome to {game_name}!")
print("=================")

# 1. Change name to string literal
name = "Tester"

# Player dictionary (add x, y)
player = {"name": name, "health": 100, "coin": 0, "x": 0, "y": 0}

# Global variables
events = ["find a coin", "meet a monster", "do nothing"]
map_size = 9


# 2–3. Move event logic into function (no prints)
def check_event():
    global player, events
    event = random.choice(events)
    if event == "find a coin":
        player["coin"] += 1
    elif event == "meet a monster":
        player["health"] -= 10
    # "do nothing" -> no change


# 6. draw_ui(x, y)
def draw_ui(x, y):
    global player, map_size
    print("=========================")
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end="  ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end="  ")
            else:
                print(".", end="  ")
        print()
    print("=========================")
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coin: {player['coin']}")
    print("=========================")


# 7. move(direction)
def move(direction):
    global player, map_size

    if direction == 'w' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 'a' and player['x'] > 0:
        player['x'] -= 1
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] += 1
    elif direction == 'd' and player['x'] < map_size - 1:
        player['x'] += 1
    else:
        print("You cannot move that way!")


# 8. main()
def main():
    draw_ui(player['x'], player['y'])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != 'q':
        move(direction)

        # Check if player reached gate
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        # Trigger event and redraw UI
        check_event()
        draw_ui(player['x'], player['y'])

        # Ask for next move
        direction = input("Your next move (w/a/s/d/q): ")


# 9. Run the program
if __name__ == '__main__':
    main()
