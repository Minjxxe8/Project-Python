from game.adventurer import Item

def fish(adventurer):
    adventurer.energy = max(0, adventurer.energy - 20)
    fish_caught = 1
    adventurer.inventory.add_item(Item("Fish", fish_caught))
    return f"You caught {fish_caught} fish !"

def search_water(adventurer):
    adventurer.energy = max(0, adventurer.energy - 20)

    if adventurer.thirsty >= 100:
        return "You found water but you are not thirsty!"
    else:
        adventurer.thirsty = min(100, adventurer.thirsty + 20)
        return "You found water and drank it!"

def sleep(adventurer):
    adventurer.energy = min(100, adventurer.energy + 20)
    adventurer.thirsty = max(0, adventurer.thirsty - 20)
    adventurer.hungry = max(0, adventurer.hungry - 20)

def woodCutting(adventurer):
    adventurer.energy = max(0, adventurer.energy - 20)
    adventurer.thirsty = max(0, adventurer.thirsty - 20)
    adventurer.hungry = max(0, adventurer.hungry - 20)
    wood_amount = 10
    adventurer.inventory.add_item(Item("Wood", wood_amount))

    crafted_part = adventurer.boat.check_and_craft(adventurer.inventory)

    message = f"You cut {wood_amount} pieces of wood !"

    return message

