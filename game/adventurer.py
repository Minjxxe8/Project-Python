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
        self.inventory = Inventory()

    def to_dict(self):
        return {
            "name": self.name,
            "days": self.days,
            "energy": self.energy,
            "thirsty": self.thirsty,
            "hungry": self.hungry,
            "health": self.health,
            "weather": self.weather,
            "inventory": self.inventory.to_dict()
        }

    def from_dict(self, data):
        self.name = data["name"]
        self.days = data["days"]
        self.energy = data["energy"]
        self.thirsty = data["thirsty"]
        self.hungry = data["hungry"]
        self.health = data["health"]
        self.weather = data["weather"]
        self.inventory.from_dict(data["inventory"])

    def is_alive(self):
        return self.thirsty > 0 and self.hungry > 0 and self.energy > 0 and self.health > 0 and self.days > 0

    def drink(self, add = 20):
        self.thirsty = min(100, self.thirsty + add)

    def eat(self):
        if self.hungry >= 100:
            return "You are not hungry!"

        food_items = ["Fish", "Meat", "Apple", "Banana", "Coconut"]
        for food in food_items:
            if food in self.inventory.items and self.inventory.items[food].quantity > 0:
                self.hungry = min(100, self.hungry + 20)
                self.inventory.remove_item(food, 1)
                return f"You have eaten {food}!"
        return "You have no food to eat!"

    def sleep(self, add = 20):
        self.energy = min(100, self.energy + add)
        self.thirsty = max(0, self.thirsty - add)
        self.days = max(0, self.days - 1)

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

    def woodCutting(self):
        self.energy = max(0, self.energy - 20)
        self.thirsty = max(0, self.thirsty - 10)
        self.hungry = max(0, self.hungry - 10)
        wood_amount = 5
        self.inventory.add_item(Item("Wood", wood_amount))
        return f"You cut {wood_amount} pieces of wood!"


class Item:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {}

    def to_dict(self):
        return {name: item.quantity for name, item in self.items.items()}

    def from_dict(self, data):
        self.items = {}
        for name, quantity in data.items():
            self.items[name] = Item(name, quantity)

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def remove_item(self, name, quantity=1):
        if name in self.items:
            self.items[name].quantity -= quantity
            if self.items[name].quantity <= 0:
                del self.items[name]

    def get_inventory(self):
        return {name: f"x{item.quantity}" for name, item in self.items.items()}

