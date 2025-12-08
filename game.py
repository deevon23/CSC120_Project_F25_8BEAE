import random

class player:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.coin = 0
  def move(self, direction, maps_size):
    if direction == "w" and self.y > 0:
      seld.y -= 1
    elif direction == "s" and self.y < map.size - 1:
      self.y += 1
    elif direction == "a" and self.x > 0:
      self.x -= 1
    elif direction == "d" and self.x < map_size - 1:
      self.x += 1
    else:
      print("You can't move that way!")

class GameMap:
    def __init__(self):
        self.size = 9

    def draw(self, player):
        for y in range(self.size):
            for x in range(self.size):
                if x == player.x and y == player.y:
                    print("P", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"Coins: {player.coin}")


class Game:
    def __init__(self):
        self.game_name = "Treasure Hunt"
        self.name = "Player1"
        self.events = ["find_coin", "nothing", "monster"]
        self.player = Player()
        self.map = GameMap()

    def check_event(self):
        event = random.choice(self.events)
        if event == "find_coin":
            print("You found a coin!")
            self.player.coin += 1
        elif event == "monster":
            print("A monster appears! You run away...")
        else:
            print("Nothing happens.")

    def play(self):
        print(f"Welcome to {self.game_name}, {self.name}!")
        print("Use W/A/S/D to move, Q to quit.\n")

        while True:
            self.map.draw(self.player)
            command = input("Move (W/A/S/D/Q): ").lower()

            if command == "q":
                print("Thanks for playing!")
                break
            elif command in ["w", "a", "s", "d"]:
                self.player.move(command, self.map.size)
                self.check_event()
            else:
                print("Invalid command!")


if __name__ == "__main__":
    Game().play()
    
