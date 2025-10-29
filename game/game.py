

from game.UI import print_ascii_survival, display_ui, display_situation
from game.boat import Boat
from game.events.events import Hunting, Explore
from game.adventurer import Adventurer
from game.events.weather import Weather
from game.voice import Voice

a = Adventurer("")
h = Hunting(a)
explorer = Explore(a)
weather = Weather()
voice = Voice()

def game():
    print_ascii_survival()
    player = input("Enter your name: ")

    display_situation(voice.intro)
    builder = Boat()
    part = builder.get_current_part()


    game_loop = True
    while game_loop:
        display_ui(a, weather, part)

        choice = input("Enter your choice: ")
        if choice == "1" :
            if weather.is_action_allowed("drink"):
                a.eat()
            else:
                display_situation("You can't drink right now due to the weather!")
        elif choice == "2" :
            if weather.is_action_allowed("eat"):
                a.eat()
            else:
                display_situation("You can't eat right now due to the weather!")
        elif choice == "3" :
            a.sleep()
        elif choice == "4":
            result = explorer.start()
            display_situation(result)
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
            reason = a.get_death_reason()
            display_situation(f"{reason}")
            game_loop = False
    return None




