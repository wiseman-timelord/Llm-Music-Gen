# scripts/temporary.py
import json

persistent_file = "./data/persistent.json"

generation_active = True  # Controls music generation loop
thread_fraction = (5, 6)  # Numerator/denominator for thread allocation
model_temperature = 0.7   # Controls LLM creativity (0.0-1.0)
audio_volume = 1.0        # Audio playback volume (0.0-1.0)

def load_config():
    global thread_fraction, model_temperature, audio_volume
    try:
        with open(persistent_file, "r") as f:
            data = json.load(f)
        config = data.get("config", {})
        thread_fraction = tuple(config.get("thread_fraction", [5, 6]))
        model_temperature = config.get("model_temperature", 0.7)
        audio_volume = config.get("audio_volume", 1.0)
    except FileNotFoundError:
        print("Warning: persistent.json not found. Using default settings.")

def save_config():
    try:
        with open(persistent_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if "config" not in data:
        data["config"] = {}
    data["config"]["thread_fraction"] = list(thread_fraction)
    data["config"]["model_temperature"] = model_temperature
    data["config"]["audio_volume"] = audio_volume
    with open(persistent_file, "w") as f:
        json.dump(data, f, indent=4)

def set_thread_fraction(new_fraction):
    global thread_fraction
    thread_fraction = new_fraction
    save_config()

def set_model_temperature(new_temperature):
    global model_temperature
    model_temperature = new_temperature
    save_config()

def set_audio_volume(new_volume):
    global audio_volume
    audio_volume = new_volume
    save_config()

# Load configuration at startup
load_config()