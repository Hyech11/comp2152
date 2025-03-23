from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        damage = self.combat_strength
        print(f"The monster dealt {damage} damage!")

        if damage <= hero.health_points:
            hero.health_points -= damage
        else:
            print("The hero has been defeated!")
            return True  # Signal to end the battle

        # End the battle immediately if health is 0 or below
        if hero.health_points <= 0:
            hero.health_points = 0  # Prevent negative health
            print("The hero has been defeated!")
            return True  # Signal to end the battle

        return False  # Continue the battle

    def __del__(self):
        print("Monster object is being deleted.")
        super().__del__()
