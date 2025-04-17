# scripts/temporary.py
import json

persistent_file = "./data/persistent.json"

generation_active = True
thread_fraction = (5, 6)
model_temperature = 0.7
audio_volume = 1.0
selected_model = "music_generation_model.Q6_K.gguf"
song_length_range = [4, 6]  # Default to 4-6 minutes

def load_config():
    """Load configuration from persistent.json."""
    global thread_fraction, model_temperature, audio_volume, selected_model, song_length_range
    try:
        with open(persistent_file, "r") as f:
            data = json.load(f)
        config = data.get("config", {})
        thread_fraction = tuple(config.get("thread_fraction", [5, 6]))
        model_temperature = config.get("model_temperature", 0.7)
        audio_volume = config.get("audio_volume", 1.0)
        selected_model = config.get("selected_model", "music_generation_model.Q6_K.gguf")
        song_length_range = config.get("song_length_range", [4, 6])
    except FileNotFoundError:
        print("Warning: persistent.json not found. Using default settings.")

def save_config():
    """Save all configurations to persistent.json."""
    data = {
        "config": {
            "thread_fraction": list(thread_fraction),
            "model_temperature": model_temperature,
            "audio_volume": audio_volume,
            "selected_model": selected_model,
            "song_length_range": song_length_range
        }
    }
    with open(persistent_file, "w") as f:
        json.dump(data, f, indent=4)

# Load configuration at startup
load_config()