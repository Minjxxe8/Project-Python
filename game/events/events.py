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



