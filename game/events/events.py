import random
from game.adventurer import Adventurer, Item


class Event:

    def __init__(self, adventurer: Adventurer):
        self.adventurer = adventurer
        self.description = ""

    def start(self):
        pass

    def get_description(self):
        return self.description


class Raining (Event):

    def start(self):
        self.adventurer.thirsty +=20
        self.description = "It's raining, you are less thirsty but you can barely seen in front of you"
        return self.description


class Hunting(Event):
    animals = {
        "poulet": {"meat": 2},
        "cochon": {"meat": 3},
        "lion": {"meat": 5}
    }

    def start(self):

        self.adventurer.energy = max(0, self.adventurer.energy - 30)
        return self.random_animal()

    def random_animal(self):
        random_animal, values = random.choice(list(self.animals.items()))
        self.adventurer.inventory.add_item(Item("Meat", values["meat"]))
        self.description = f"You have chased a {random_animal} and got {values['meat']} meat!"
        return self.description

class Discovery(Event):
    fruits = {
        "apple": 2,
        "banana": 3,
        "coconut": 1,
    }

    def start(self):
        random_fruit, quantity = random.choice(list(self.fruits.items()))
        self.adventurer.inventory.add_item(Item(random_fruit, quantity))
        self.description = f"You found {quantity} {random_fruit}(s)!"
        return self.description

class Fishing(Event):
    fish = {
        "salmon": "10",
        "bluefish": "20",
        "Carp": "50"
    }

    def start(self):

        self.adventurer.energy = max(0, self.adventurer.energy - 30)
        return self.random_fish()

    def random_fish(self):
         random_fish, value = (random.choice(list(self.fish.items())))
         self.adventurer.hungry = min(100, self.adventurer.hungry + int(value))
         self.description = f"you have fishing a {random_fish} , you have gained {value} point of hunger, but you have lost energy"
         return self.description

class Explore(Event):

    def start(self):
        event_type = random.choice([Discovery, Hunting, Fishing])
        event = event_type(self.adventurer)
        result = event.start()

        self.description = f"While exploring, {event.get_description()}"
        return self.description
