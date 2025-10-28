from game.UI import print_ascii_survival, display_ui, display_situation
from game.boat import Boat
from game.events.events import Hunting, Discovery
from game.adventurer import Adventurer
from game.voice import Voice

a = Adventurer("non")
h = Hunting(a)

voice = Voice()

def game():
    print_ascii_survival()
    player = input("Enter your name: ")

    display_situation(voice.intro)
    builder = Boat()
    part = builder.get_current_part()


    game_loop = True
    while game_loop:
        display_ui(a, part)

        choice = input("Enter your choice: ")
        if choice == "1" :
            a.drink()
        elif choice == "2" :
            a.eat()
        elif choice == "3" :
            a.sleep()
        elif choice == "h".lower() :
            h.start()
        elif choice == "q" :
            print("You have quit the game, but don't worry, the game is saved !")
            game_loop = False
        elif choice == "i".lower():
            print("You have open the inventory (technically)")
        else :
            print("Its not on the choices, choose another one")

        if not a.is_alive():
            print("You are dead")
            game_loop = False
    return None




