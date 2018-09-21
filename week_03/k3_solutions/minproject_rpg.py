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

        if hero_roll > opponent_roll:
            #print(type(hero_roll))
            #print(type(opponent_roll))
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
        return f"Opponent {self.name}" # at Lvl {self.level}"

class KindOpponent(Opponent):
    """ Way more kind than the general opponent"""
    def __init__(self, name):
        Opponent.__init__(self, name, 0)

    def __str__(self):
        return f"Kind Opponent {self.name}" # at Lvl {self.level}"


class SofterOpponent(Opponent):
    """ Somewhat softer than the general opponent
        Starts at low level but is willing to collaborate,
        or at least pretends to.
        Has a method collaborate() that can take hero's level
        multiply it, so opponent will come out way better.

    """
    def __init__(self, name):
        Opponent.__init__(self, name, 0)

    def __str__(self):
        return f"Softer Opponent {self.name} at Lvl {self.level}"

    def collaborate(self, hero):
        hero_roll = random.randint(1, 6) * hero.level
        opponent_roll = random.randint(1, 6) * self.level

        if hero_roll > opponent_roll:
            self.level = hero.level * 10
            return self.level
        else:
            return self.level



if __name__ == '__main__':
    h = Hero("Caden", 30)
    print(h)

