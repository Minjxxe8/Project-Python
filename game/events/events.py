import random
from game.adventurer import Adventurer


class Event:

    def __init__(self, adventurer: Adventurer):
        self.adventurer = adventurer

    def start(self):
        pass

    def random_event(self):
        pass


class Raining (Event):

    def start(self):
        self.adventurer.thirsty +=20
        pass

class Hunting(Event):
    animals = {
        "poulet": "10",
        "cochon": "20",
        "lion": "50"
    }

    def start(self):

        self.adventurer.energy = max(0, self.adventurer.energy - 30)
        self.random_animal()

    def random_animal(self):
         random_animal, value = (random.choice(list(self.animals.items())))
         print(random_animal, value)

         self.adventurer.hungry = min(100, self.adventurer.hungry + int(value))

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


'''
class RandomEvent(Event) :
    hunting = Hunting()
    raining = Raining()
    discovery = Discovery()

    random_event = [hunting, raining, discovery]

    def start(self):
        print(random.choice(list(self.random_event)))'''

