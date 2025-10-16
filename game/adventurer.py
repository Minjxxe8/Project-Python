class Adventurer :
    def __init__(self, name, thirsty=100, hungry=100, energy=100):
        self.name = name
        self.thirsty = thirsty
        self.hungry = hungry
        self.energy = energy

    def is_alive(self):
        return self.thirsty > 0 and self.hungry > 0 and self.energy > 0

    def drink(self, add = 20):
        self.thirsty = max(100, self.thirsty + add)

    def eat(self, add = 20):
        self.hungry = max(100, self.hungry + add)

    def sleep(self, add = 20):
        self.energy = max(100, self.energy + add)