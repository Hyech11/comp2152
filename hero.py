from character import Character

class Hero(Character):
    def __init__(self, weapon):
        super().__init__()
        self.weapon = weapon

    def hero_attacks(self, monster):
        weapon_name = self.weapon["name"]
        damage = self.weapon["damage"]

        # Optional bonus damage based on weapon logic
        if weapon_name == "Spear" and monster.health_points < 20:
            damage += 5
        elif weapon_name == "Bow":
            damage += 2  # ranged bonus

        print(f"The hero attacks with {weapon_name}, dealing {damage} damage!")

        monster.health_points -= damage
        if monster.health_points <= 0:
            monster.health_points = 0
            print("The monster has been defeated!")
            return True  # End battle

        return False  # Continue battle

    def __del__(self):
        print("Hero object is being deleted.")
        super().__del__()
