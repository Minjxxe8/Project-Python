import json

from game.adventurer import Item


class Boat:
    def __init__(self, json_path="data/history-data.json"):
        with open(json_path, "r") as file:
            data = json.load(file)

        self.parts = data["boat_parts"]
        self.progress = 0

    def to_dict(self):
        return {
            "progress": self.progress
        }

    def from_dict(self, data):
        self.progress = data["progress"]

    def get_current_part(self):
        if self.progress < len(self.parts):
            return self.parts[self.progress]
        return None

    def get_next_part(self):
        if self.progress < len(self.parts):
            self.progress += 1
            return self.parts[self.progress]
        return None

    def check_and_craft(self, inventory):
        current_part = self.get_current_part()
        if not current_part:
            return None

        can_craft = True
        for resource, amount_needed in current_part["resources"].items():
            if resource not in inventory.items:
                can_craft = False
                break
            if inventory.items[resource].quantity < amount_needed:
                can_craft = False
                break

        if can_craft:
            for resource, amount_needed in current_part["resources"].items():
                inventory.remove_item(resource, amount_needed)
            inventory.add_item(Item(current_part["name"], 1))

            self.progress += 1

            return current_part

        return None

    def is_complete(self):
        return self.progress >= len(self.parts)