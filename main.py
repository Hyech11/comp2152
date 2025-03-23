import os
import platform
import random
from hero import Hero
from monster import Monster
import functions

# Weapon list (Weapon Mastery System)
weapons = [
    {"name": "Sword", "damage": 10},
    {"name": "Spear", "damage": 12},
    {"name": "Bow", "damage": 8},
    {"name": "Dagger", "damage": 9}
]

# OS and Python info
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Load saved monster kill count
def load_monster_kills():
    try:
        with open("save.txt", "r") as file:
            data = file.read().strip()
            return int(data) if data.isdigit() else 0
    except FileNotFoundError:
        return 0

previous_kills = load_monster_kills()
print(f"Total monsters defeated in previous games: {previous_kills}")

# Weapon selection
print("\nChoose your weapon:")
for idx, w in enumerate(weapons):
    print(f"{idx + 1}. {w['name']} (Damage: {w['damage']})")

selected_index = -1
while selected_index not in range(1, len(weapons) + 1):
    try:
        selected_index = int(input("Enter weapon number: "))
    except ValueError:
        print("Please enter a valid number.")

selected_weapon = weapons[selected_index - 1]
print(f"You have chosen: {selected_weapon['name']}")

# Instantiate characters
hero = Hero(selected_weapon)
monster = Monster()
monster_kills = 0

# Dream level input
dream_level = functions.validate_input()
print(f"You have entered dream level {dream_level}.")

# Fight begins
while hero.health_points > 0 and monster.health_points > 0:
    print(f"\nHero HP: {hero.health_points} | Monster HP: {monster.health_points}")

    if hero.hero_attacks(monster):
        monster_kills += 1
        break

    if monster.monster_attacks(hero):
        break

# Save game progress
total_kills = previous_kills + monster_kills
with open("save.txt", "w") as file:
    file.write(str(total_kills))

print(f"Game over. Total monsters defeated: {total_kills}")
