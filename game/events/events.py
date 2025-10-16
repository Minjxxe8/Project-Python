import random

class Event:

    def start(self):
        pass

    def random_event(self):
        pass


class Raining (Event):

    def start(self):
        #soif -= 10
        pass

class Hunting(Event):
    animals = {
        "poulet": "10",
        "cochon": "20",
        "lion": "50"
    }

    def starting(self):
        #Il gagne à chaque fois, mais ça lui prend beacoup d'énergies
        #energie -= 20
        #print(f"energie : {energie}")
        self.random_animal()
        pass

    def random_animal(self):
         random_animal = (random.choice(list(self.animals.items())))
         print(random_animal)
         #faim -= animal key

class Discovery (Event):

    def start(self):
        self.random_finding()


    def random_finding(self):
        random_finding = (random.choice(list(self.ressources)))
        print(random_finding)


class RandomEvent :
    hunting = Hunting()
    raining = Raining()
    discovery = Discovery()

    random_event = [hunting, raining, discovery]

    def start(self):
        print(random.choice(list(self.random_event)))

