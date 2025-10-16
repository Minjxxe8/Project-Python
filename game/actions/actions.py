def fish(adventurer):
    adventurer.hungry = min(100, adventurer.hungry + 20)
    adventurer.energy = max(0, adventurer.energy - 20)

def search_water(adventurer):
    adventurer.thirsty = min(100, adventurer.thirsty + 20)
    adventurer.energy = max(0, adventurer.energy - 20)

def sleep(adventurer):
    adventurer.energy = min(100, adventurer.energy + 20)
    adventurer.thirsty = max(0, adventurer.thirsty - 20)
    adventurer.hungry = max(0, adventurer.hungry - 20)
