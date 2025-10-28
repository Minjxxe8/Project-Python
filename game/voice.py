import json


class Voice:
    def __init__(self, json_path="data/history-data.json"):
        with open(json_path, "r") as file:
            data = json.load(file)

        self.intro = data["intro"]["voice"]
        self.outro = data["outro"]["voice"]

    def play_intro(self):
        print(self.intro)

    def play_outro(self):
        print(self.outro)