    diceOptions = list(range(1,7))

    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

    print("Available weapons: ", ', '. join(weapons))

    def get_combat_stregth(prompt):
        while True:
            try:
                value = int(input(prompt))
                if 1 <= value <= 6:
                    return value
                else:
                    print("invalid input! Please enter a number between 1-6")
            except ValueError:
                print("invalid input! Please enter a number between 1-6")

combatStregth = get_combat_stregth("Enter your combat stregth (1-6): ")
combatStregth = get_combat_stregth("Enter monster's combat stregth (1-6): ")
