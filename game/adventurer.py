class Adventurer :
    def __init__(self, name, thirsty=100, hungry=100, energy=100):
        self.name = name
        self.thirsty = thirsty
        self.hungry = hungry
        self.energy = energy

    def is_alive(self):
        return self.thirsty > 0 and self.hungry > 0 and self.energy > 0

    def drink(self, add_drink = 20):
        self.thirsty = min(100, self.thirsty + add_drink)

    def eat(self, add_eat = 20):
        self.hungry = min(100, self.hungry + add_eat)

    def sleep(self, add_energy = 20):
        self.energy = min(100, self.energy + add_energy)

