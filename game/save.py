import json
import os


class Save:
    def __init__(self, default_filename="save.json"):
        self.default_filename = default_filename

    def save_game(self, adventurer, boat, weather, filename=None):
        if filename is None:
            filename = self.default_filename

        save_data = {
            "adventurer": adventurer.to_dict(),
            "boat": boat.to_dict(),
            "weather": weather.to_dict()
        }

        try:
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    def load_game(self, filename=None):
        if filename is None:
            filename = self.default_filename

        if not os.path.exists(filename):
            return None

        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading game: {e}")
            return None