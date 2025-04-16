# requisites.py
import os
import subprocess
import json
import venv
from huggingface_hub import hf_hub_download

def create_venv():
    venv_dir = "./venv"
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)
    return venv_dir

def install_dependencies(venv_dir):
    pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
    packages = [
        "llama-cpp-python",
        "rich",
        "pretty_midi",
        "pydub",
        "simpleaudio",
        "numpy",
        "huggingface_hub"
    ]
    requirements_content = "\n".join(packages) + "\n"
    with open("./data/requirements.txt", "w") as f:
        f.write(requirements_content)
    
    print("Installing dependencies...")
    for package in packages:
        subprocess.check_call([pip_path, "install", package])

def download_model():
    model_repo = "nagayama0706/music_generation_model-GGUF"
    model_file = "music_generation_model.Q6_K.gguf"
    download_path = "./data/"
    os.makedirs(download_path, exist_ok=True)
    hf_hub_download(repo_id=model_repo, filename=model_file, local_dir=download_path)
    print(f"Model downloaded to {download_path}{model_file}")

def create_persistent_json():
    template = {
        "default_prompt": {
            "system": "You are a music generation assistant. Generate a MIDI sequence for a {style} song in the format: pitch,start_time,duration,velocity per line.",
            "user": "Generate a MIDI sequence for a {style} song."
        }
    }
    os.makedirs("./data", exist_ok=True)
    with open("./data/persistent.json", "w") as f:
        json.dump(template, f, indent=4)

def main():
    os.makedirs("./data/raw", exist_ok=True)
    os.makedirs("./Output", exist_ok=True)
    venv_dir = create_venv()
    install_dependencies(venv_dir)
    download_model()
    create_persistent_json()
    print("[bold green]Setup complete. Run Llm-Music-Gen.bat to start.[/bold green]")

if __name__ == "__main__":
    main()