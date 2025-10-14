from game.UI import print_ascii_survival

player = ""
choices = {
    "1": "First choice",
    "2": "Second choice",
    "3": "Third choice",
    "4": "Fourth choice",
    "5": "Fifth choice",
}

def game():
    print_ascii_survival()
    player = input("Enter your name: ")
    print(f"Hello {player}!")
    game_loop = True
    while game_loop:
        choice = input("Enter your choice: ")
        if choice in choices:
            print(f"{choices[choice]} choice selected.")
        elif choice.lower() == "q":
            game_loop = False
        elif choice.lower() == "i":
            print("You have open the inventory")
        else :
            print("Its not on the choices, choose another one")
    return None




