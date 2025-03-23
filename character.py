import random

class Character:
    def __init__(self):
        self._combat_strength = random.randint(1, 100)
        self._health_points = random.randint(50, 150)

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:
            self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self._health_points = value

    def __del__(self):
        print(f"{self.__class__.__name__} object is being deleted by the garbage collector.")
