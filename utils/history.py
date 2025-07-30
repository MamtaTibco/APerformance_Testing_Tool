# utils/history.py
import json
import os
from datetime import datetime

HISTORY_FILE = "history_tibcoresponse.json"


def load_history_data():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_history_data(entry):
    history = load_history_data()
    entry["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.insert(0, entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
