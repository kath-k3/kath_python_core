import random

# create a Hero blueprint

class Hero():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # Hero can attack the opponent
    def attack(self, opponent):
        hero_roll = random.randint(1, 6) * self.level
        opponent_roll = random.randint(1, 6) * opponent.level

        if hero_roll >= opponent_roll:
            return True
        else:
            return False


    def __str__(self):
        return f"{self.name}, Lvl: {self.level}"

# simulate a dice roll to determine who wins (True/False)

# create an Opponent blueprint
class Opponent():
    """docstr for the Opponent"""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"Opponent {self.name} at Lvl {self.level}"

if __name__ == '__main__':
    h = Hero("Caden", 30)
    print(h)

