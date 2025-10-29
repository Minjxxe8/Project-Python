import random
from game.adventurer import Adventurer


class Event:

    def __init__(self, adventurer: Adventurer):
        self.adventurer = adventurer
        self.description = ""

    def start(self):
        pass

    def get_description(self):
        return self.description

class Hunting(Event):
    animals = {
        "poulet": "10",
        "cochon": "20",
        "lion": "50"
    }

    def start(self):

        self.adventurer.energy = max(0, self.adventurer.energy - 30)
        return self.random_animal()

    def random_animal(self):
         random_animal, value = (random.choice(list(self.animals.items())))
         self.adventurer.hungry = min(100, self.adventurer.hungry + int(value))
         self.description = f"You have chase a {random_animal} , you have gained {value} point of hunger, but you have lost energy"
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

class Discovery(Event):
    fruits = {
        "apple": "10",
        "banana": "20",
        "coconut": "30",
    }

    def start(self):
        random_fruit, value = (random.choice(list(self.fruits.items())))
        print(random_fruit, value)
        self.adventurer.hungry = min(100, self.adventurer.hungry + int(value))
        self.description = f"you have found : {random_fruit}, you have gained {value} point of hunger !"
        return self.description

class Explore(Event):

    def start(self):
        event_type = random.choice([Discovery, Hunting, Fishing])
        event = event_type(self.adventurer)
        result = event.start()

        self.description = f"While exploring, {event.get_description()}"
        return self.description