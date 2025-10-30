from game.UI import print_ascii_survival, display_ui, display_situation
from game.boat import Boat
from game.events.events import Hunting, Discovery, Explore
from game.adventurer import Adventurer, Item, Inventory
from game.events.weather import Weather
from game.save import Save
from game.voice import Voice

a = Adventurer("")
h = Hunting(a)
explorer = Explore(a)
weather = Weather()
voice = Voice()
inventory = a.inventory.get_inventory()
save = Save()


def game():
    print_ascii_survival()

    save_data = save.load_game()

    if save_data:
        choice = input("A save file was found! Load it? (y/n): ").lower()
        if choice == 'y':
            a.from_dict(save_data["adventurer"])
            builder = Boat()
            builder.from_dict(save_data["boat"])
            weather.from_dict(save_data["weather"])

            print(f"\nWelcome back, {a.name}!")
            input("Press Enter to continue...")
        else:
            a.name = input("Enter your name: ")
            builder = Boat()
    else:
        a.name = input("Enter your name: ")
        builder = Boat()


    display_situation(voice.intro)
    builder = Boat()
    part = builder.get_current_part()

    game_loop = True
    while game_loop:
        display_ui(a, weather, part)

        choice = input("Enter your choice: ")
        if choice == "1":
            if weather.is_action_allowed("drink"):
                a.eat()
            else:
                display_situation("You can't drink right now due to the weather!")
        elif choice == "2":
            if weather.is_action_allowed("eat"):
                a.eat()
            else:
                display_situation("You can't eat right now due to the weather!")
        elif choice == "3":
            a.sleep()
        elif choice == "4":
            result = explorer.start()
            display_situation(result)
        elif choice == "5":
            message = a.woodCutting()
            crafted_part = builder.check_and_craft(a.inventory)

            if crafted_part:
                message += f"\n\n=== CRAFT ==="
                message += f"\n✓ {crafted_part['name']} completed!"
                message += f"\n====================="

                part = builder.get_current_part()

                if builder.is_complete():
                    message += f"\n\nTHE BOAT IS COMPLETE, YOU CAN ESCAPE, WELL PLAYEDDDDD!!!!!"
                elif part:
                    wood_needed = part["resources"]["Wood"]
                    message += f"\n\nNext part: {part['name']}"
                    message += f"\nResources needed: {wood_needed}"
            print(message)
            input("Press enter to continue...")
        elif choice == "h".lower() :
            builder.get_next_part()
            part = builder.get_current_part()
        elif choice == "q" :
            if save.save_game(a, builder, weather):
                print("Game saved successfully!")
            print("You have quit the game, but don't worry, the game is saved !")
            game_loop = False
        elif choice == "i".lower():
            print("\n=== Inventory ===")
            inv = a.inventory.get_inventory()
            if inv:
                for name, quantity in inv.items():
                    print(f"{name}: {quantity}")
            else:
                print("Your inventory is empty.")
                print("\n" * 2)
            print("=================\n")
            input("Press Enter to continue...")
        else :
            print("Its not on the choices, choose another one")

        if not a.is_alive():
            reason = a.get_death_reason()
            display_situation(f"{reason}")
            game_loop = False
    return None
