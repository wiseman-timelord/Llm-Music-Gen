# requisites.py
import os
import shutil
import subprocess
import json
import venv
from huggingface_hub import hf_hub_download

def clean_install():
    """Delete existing ./venv and ./data directories for a clean install."""
    for dir in ["./venv", "./data"]:
        if os.path.exists(dir):
            shutil.rmtree(dir)

def create_directories():
    """Create all necessary directories for the project."""
    dirs = ["./data", "./models", "./data/raw", "./Output"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def create_persistent_json():
    """Create persistent.json with default configuration."""
    template = {
        "config": {
            "thread_fraction": [5, 6],
            "model_temperature": 0.7,
            "audio_volume": 1.0,
            "selected_model": "music_generation_model.Q6_K.gguf"
        }
    }
    with open("./data/persistent.json", "w") as f:
        json.dump(template, f, indent=4)

def download_model():
    """Download the default model to ./models/."""
    model_repo = "nagayama0706/music_generation_model-GGUF"
    model_file = "music_generation_model.Q6_K.gguf"
    download_path = "./models/"
    hf_hub_download(repo_id=model_repo, filename=model_file, local_dir=download_path)
    print(f"Model downloaded to {download_path}{model_file}")

def create_venv():
    """Create a virtual environment."""
    venv_dir = "./venv"
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_dir)
    return venv_dir

def upgrade_venv_tools(venv_dir):
    """Upgrade pip and other essential tools in the virtual environment."""
    pip_executable = os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "pip")
    subprocess.run([pip_executable, "install", "--upgrade", "pip"], check=True)

def install_dependencies(venv_dir):
    """Install required dependencies into the virtual environment."""
    pip_executable = os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "pip")
    dependencies = [
        "huggingface_hub",
        "rich",
        "pretty_midi",
        "pydub",
        "simpleaudio",
        "numpy",
        "llama-cpp-python"
    ]
    for dep in dependencies:
        subprocess.run([pip_executable, "install", dep], check=True)

def main():
    clean_install()  # Clean existing directories
    create_directories()  # Create necessary directories
    venv_dir = create_venv()  # Create the virtual environment
    upgrade_venv_tools(venv_dir)  # Upgrade pip in the virtual environment
    install_dependencies(venv_dir)  # Install dependencies into the virtual environment
    download_model()  # Download the model
    create_persistent_json()  # Create persistent.json
    print("[bold green]Setup complete. Run Llm-Music-Gen.bat to start.[/bold green]")

if __name__ == "__main__":
    main()