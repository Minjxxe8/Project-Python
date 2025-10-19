from game.UI import print_ascii_survival
from game.events.events import Hunting, Discovery
from game.adventurer import Adventurer

a = Adventurer("non")


def game():
    print_ascii_survival()
    player = input("Enter your name: ")
    print(f"Hello {player}!")
    game_loop = True
    while game_loop:
        choice = input("Enter your choice: ")
        if choice == "d".lower() :
            a.drink()
        elif choice == "e".lower() :
            a.eat()
        elif choice == "s".lower() :
            a.sleep()
        else :
            print("Its not on the choices, choose another one")

        a.print_adventurer_state()
    return None




