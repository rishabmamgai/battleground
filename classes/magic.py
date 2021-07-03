import random

class Spell:
    def __init__(self, name, cost, dmg, types):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.types = types

    def generate_damage(self):
        low = self.dmg - 10
        high = self.dmg + 10
        return random.randrange(low, high)