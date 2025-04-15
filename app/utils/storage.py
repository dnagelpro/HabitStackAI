import json
import os

DATA_FILE = os.path.join("data", "habits.json")

def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_habits(habits):
    with open(DATA_FILE, "w") as file:
        json.dump(habits, file, indent=2)
