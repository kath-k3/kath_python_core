import random
from minproject_rpg import Hero, Opponent, KindOpponent, SofterOpponent
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
        KindOpponent("KinddMan"),
        SofterOpponent("Softie")
        ]
    #print(len(opponents))
    #print(type(opponents))
    #for i in opponents:
    #    print(i)

    # create the hero
    hero = Hero("Caden", 2000)

    #ask user for input and run until quit
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
            if "Kind" in str(opponent):
                #opponents.clear()
                print("You hit the hot spot! All opponents gone, game over!")
                break
            if hero.attack(opponent):
                opponents.remove(opponent)
                print("You win this round, we removed: ", opponent)

            else:
                print("You lost..")
                time.sleep(5)
                print("You can play again!")

if __name__ == '__main__':
    main()
