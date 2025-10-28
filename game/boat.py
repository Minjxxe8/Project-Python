import json


class Boat:
    def __init__(self, json_path="data/history-data.json"):
        with open(json_path, "r") as file:
            data = json.load(file)

        self.parts = data["boat_parts"]
        self.progress = 0

    def get_current_part(self):
        if self.progress < len(self.parts):
            return self.parts[self.progress]
        return None

    def get_next_part(self):
        if self.progress + 1 < len(self.parts):
            return self.parts[self.progress + 1]
        return None

    #def can_buil_part(self):
    #Implémenter ça avec l'inventaire pour vérifier si il peut build la partie du boat

    #def buil(self) :

    def is_complete(self):
        return self.progress >= len(self.parts)