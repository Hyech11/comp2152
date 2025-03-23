import os
import random

def validate_input():
    while True:
        try:
            level = int(input("Enter dream level (0-3): "))
            if 0 <= level <= 3:
                return level
            else:
                print("Please enter a number between 0 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            return lines[-1].strip() if lines else None
    except FileNotFoundError:
        return None

def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
