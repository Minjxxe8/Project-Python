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


class Raining (Event):

    def start(self):
        self.adventurer.thirsty +=20
        self.description = "It's raining, you are less thirsty but you can barely seen in front of you"
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
        self.description = f"You have found : {random_fruit}, you have gained {value} point of hunger !"
        return self.description


class EventManager:
    def __init__(self, adventurer):
        self.adventurer = adventurer
        self.available_events = [Raining, Hunting, Discovery]

    def start_random_event(self):
        event_class = random.choice(self.available_events)
        event = event_class(self.adventurer)
        return event.start()

    def start_specific_event(self, event_class):
        event = event_class(self.adventurer)
        return event.start()
