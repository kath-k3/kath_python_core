import random
from minproject_rpg import Hero, Opponent
import time

#make a main()function
def main():
    print("Hey, welcome to the game!\n")
    play_game()

# create play_game() function with the logic
def play_game():
    # create opponents
    opponents = [
        Opponent("Messi", 99),
        Opponent("Ratikic", 94),
        Opponent("Pique", 89),
        ]

    # create the hero
    hero = Hero("Caden", 100)

    #ask user for input and run until quirt
    while True:
        # end the game if all the opponents are defeated
        if len(opponents) <= 0:
            print("You won the game!")
            break

        cmd = input("enter [a] for attack or [q] to quit: ")
        #check input validity
        while cmd not in ["a", "q"]:
            cmd = input ("enter [a] for attack or [q] to quit: ")
        if cmd == "q":
            print("bye!")
            exit()
        elif cmd == "a":
            opponent = random.choice(opponents)
            if hero.attack(opponent):
                print("You win!")
                opponents.remove(opponent)
            else:
                print("You lost..")
                time.sleep(5)
                print("You can play again!")

if __name__ == '__main__':
    main()
