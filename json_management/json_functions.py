import json
import os

def save_json(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving JSON to {filename}: {e}")

def load_json(filename, default=None):
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: Failed to decode JSON from {filename}. Returning default value.")
        return default
    except Exception as e:
        print(f"Error loading JSON from {filename}: {e}")
        return default
