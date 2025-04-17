# scripts/models.py
from llama_cpp import Llama
from scripts.prompts import load_prompt_template
from scripts.temporary import model_temperature, song_length_range
import random

def load_model(model_path, n_threads):
    try:
        model = Llama(model_path=model_path, n_threads=n_threads, verbose=False)
        return model
    except Exception as e:
        raise Exception(f"Failed to load model: {e}")

def generate_music(model, style):
    prompt = load_prompt_template(style)
    try:
        min_len, max_len = song_length_range
        if min_len == max_len:
            song_length = min_len
        else:
            song_length = random.uniform(min_len, max_len)
        tokens_per_minute = 256  # Assumption: 256 tokens ≈ 1 minute
        max_tokens = int(song_length * tokens_per_minute)
        output = model(prompt=prompt, max_tokens=max_tokens, temperature=model_temperature, top_k=50, top_p=0.95)
        return output["choices"][0]["text"].strip()
    except Exception as e:
        raise Exception(f"Music generation failed: {e}")