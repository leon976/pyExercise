import time
import random

# Define a function to print a colored message
def print_color(text, color):
    print(f"{color}{text}\033[0m")

# Print a colored welcoming message
print_color("**********************************************", "\033[38m")
print_color("*                                            *", "\033[32m")
print_color("*                                            *", "\033[32m")
print_color("*              WELCOME TO PUBG RPG           *", "\033[33m")
print_color("*                                            *", "\033[32m")
print_color("*                                            *", "\033[32m")
print_color("**********************************************", "\033[39m")
print_color("\nSurvive the battle and become the last player standing!\n", "\033[36m")
time.sleep(1)

# ANSI color codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Define lion and tiger classes
class Lion:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Tiger:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

# Define the game loop
def game_loop():
    # Create the player and enemy
    lion = Lion("Lion", 100, 20)
    tiger = Tiger("Tiger", 100, 20)

    print("You are entering into the battlefield...")

    # Game loop
    while True:
        print(f"\n{lion.name} has {lion.health} health left.")
        print(f"{tiger.name} has {tiger.health} health left.")

        # lion turn
        player_choice = input("\nDo you want to attack (a) or heal (h)? ")
        if player_choice == "a":
            tiger.health -= lion.damage
            print(f"lion attack with it sharp claws {tiger.name} for {lion.damage} damage!")
        elif player_choice == "h":
            lion.health += 20
            print(f"You heal yourself for 20 health points!")
        else:
            print("Invalid input. Try again.")
            continue

        # Check if enemy is defeated
        if tiger.health <= 0:
            print(f"\n{tiger.name} has been defeated!")
            break

        # tiger turn
        enemy_choice = random.choice(["a", "h"])
        if enemy_choice == "a":
            lion.health -= tiger.damage
            print(f"{tiger.name} pounces on its prey for {tiger.damage} damage!")
        elif enemy_choice == "h":
            tiger.health += 10
            print(f"{tiger.name} heals himself for 10 health points!")

        # Check if player is defeated
        if lion.health <= 0:
            print(f"\n{lion.name} has been defeated!")
            break

# Call the game loop
game_loop()
