import shutil

from game.adventurer import Adventurer
from game.events.events import EventManager


def print_ascii_survival():
    print(r"""
  .-')                _  .-')        (`-.                 (`-.     ('-.               
 ( OO ).             ( \( -O )     _(OO  )_             _(OO  )_  ( OO ).-.           
(_)---\_) ,--. ,--.   ,------. ,--(_/   ,. \ ,-.-') ,--(_/   ,. \ / . --. / ,--.      
/    _ |  |  | |  |   |   /`. '\   \   /(__/ |  |OO)\   \   /(__/ | \-.  \  |  |.-')  
\  :` `.  |  | | .-') |  /  | | \   \ /   /  |  |  \ \   \ /   /.-'-'  |  | |  | OO ) 
 '..`''.) |  |_|( OO )|  |_.' |  \   '   /,  |  |(_/  \   '   /, \| |_.'  | |  |`-' | 
.-._)   \ |  | | `-' /|  .  '.'   \     /__),|  |_.'   \     /__) |  .-.  |(|  '---.' 
\       /('  '-'(_.-' |  |\  \     \   /   (_|  |       \   /     |  | |  | |      |  
 `-----'   `-----'    `--' '--'     `-'      `--'        `-'      `--' `--' `------'     
    """)

def clear_screen():
    print("\n" * 5)

def center_content(content_lines):
    terminal_height = shutil.get_terminal_size().lines
    padding = max(0, (terminal_height - content_lines) // 2)
    return "\n" * padding



def display_ui(adventurer, current_part=None):
    event_manager = EventManager(adventurer)
    event = event_manager.start_random_event()
    clear_screen()
    print(center_content(20))

    # En-tête
    print("=" * 50)
    print("                    SURVIVAL")
    print("=" * 50)

    print(f"Thirst:     [{create_bar(adventurer.thirsty)}] {adventurer.thirsty}%")
    print(f"Hunger:     [{create_bar(adventurer.hungry)}] {adventurer.hungry}%")
    print(f"Energy:     [{create_bar(adventurer.energy)}] {adventurer.energy}%")

    print("=" * 50)

    print("\nSituation:")
    if current_part:
        print(f"Current objective: {current_part['name']}")
        print(current_part['help'])
    else:
        print("You are surviving on the island...")

    print("=" * 50)

    print("\nEvent:")
    print(event)

    print("=" * 50)

    print("\nAction:")
    print("  [1] Drink    [2] Eat    [3] Sleep    [5] Cut Wood")

    print("=" * 50)

    print("\n[Q] Quit" + " " * 25 + "[I] Inventory")
    print("\n" * 5)


def create_bar(value, length=10):
    filled = int((value / 100) * length)
    bar = "█" * filled + "░" * (length - filled)
    return bar


def display_situation(voice_text):
    clear_screen()
    print("="*50)
    print("SITUATION:")
    print(voice_text)
    print("\n[OK] Press Enter to continue")
    input()
