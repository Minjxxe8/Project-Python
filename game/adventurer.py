from game.events.weather import Weather

class Adventurer :
    def __init__(self, name, days=50, weather: Weather="rain", thirsty=100, hungry=100, energy=100, health=100):
        self.name = name
        self.days = days
        self.thirsty = thirsty
        self.hungry = hungry
        self.energy = energy
        self.health = health
        self.weather = weather

    def is_alive(self):
        return self.thirsty > 0 and self.hungry > 0 and self.energy > 0 and self.health > 0 and self.days > 0

    def drink(self, add = 20):
        self.thirsty = min(100, self.thirsty + add)

    def eat(self, add=20):
        self.hungry = min(100, self.hungry + add)

    def sleep(self, add = 20):
        self.energy = min(100, self.energy + add)
        self.thirsty = max(0, self.thirsty - add)
        self.days = max(0, self.days - 1)

    def health(self, add = 20):
        self.energy = min(100, self.energy + add)

    def print_adventurer_state(self):
        print(f"energy : {self.energy}")
        print(f"thirsty : {self.thirsty}")
        print(f"hungry : {self.hungry}")
        print(f"health : {self.health}")

    def get_death_reason(self):
        if self.days <= 0:
            return "You ran out of time, nobody can help you lol"
        if self.thirsty <= 0:
            return "Did you forgot to drink ? Anyways, you're dead because of this."
        if self.hungry <= 0:
            return "Yooo did you think that you can live without eat ??"
        if self.energy <= 0:
            return "You died of exhaustion, think to sleep sometimes..."
        if self.health <= 0:
            return "Your health reached zero..."
        return "Unknown cause"