class Adventurer :
    def __init__(self, name, thirsty=100, hungry=100, energy=100):
        self.name = name
        self.thirsty = thirsty
        self.hungry = hungry
        self.energy = energy
        self.inventory = Inventory()

    def is_alive(self):
        return self.thirsty > 0 and self.hungry > 0 and self.energy > 0

    def drink(self, add = 20):
        self.thirsty = min(100, self.thirsty + add)

    def eat(self, add = 20):
        self.hungry = min(100, self.hungry + add)

    def sleep(self, add = 20):
        self.energy = min(100, self.energy + add)

    def print_adventurer_state(self):
        print(f"energy : {self.energy}")
        print(f"thirsty : {self.thirsty}")
        print(f"hungry : {self.hungry}")

class Item:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {}

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

