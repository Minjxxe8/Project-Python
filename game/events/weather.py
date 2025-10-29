import random


class Weather:
    def __init__(self):
        self.current_weather = "sunny"
        self.description = self.weather[self.current_weather]

    weather = {
        "rain": "It's raining, you can barely seen and you can't eat under the rain.",
        "lightning": "There is a big lighting ! You can't do anything, go to sleep, or go get somewhere safe",
        "cold": "It’s cold, your hands are frozen and your movements are slow and difficult",
        "sunny": "There is a big sun, a good time to farm for your boat !"
    }

    restrictions = {
        "rain": ["eat"],
        "lightning": ["eat", "drink"],
        "cold": ["drink"],
        "sunny": []
    }

    def generate_weather(self, days):
        if days == 50:
            self.current_weather = "rain"
        elif days % 3 == 0:
            self.current_weather = self.random_weather()
        else:
            self.current_weather = "sunny"

        self.description = self.weather[self.current_weather]
        return self.description

    def random_weather(self):
        random_weather = random.choice(list(self.weather.keys()))
        return random_weather

    def get_weather(self):
        return self.current_weather

    def get_description(self):
        return self.description

    def is_action_allowed(self, action: str) -> bool:
        return action not in self.restrictions.get(self.current_weather, [])