import json
import os

def load_settings():
    try:
        with open("program_settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"order": []}

def save_settings(data):
    with open("program_settings.json", "w") as f:
        json.dump(data, f, indent=4)