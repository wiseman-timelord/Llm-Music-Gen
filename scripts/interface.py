# scripts/interface.py
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from scripts.temporary import thread_fraction, model_temperature, audio_volume, selected_model

console = Console()

def select_model():
    """Allow the user to select a model from the ./models directory."""
    console.clear()
    title = Text("Select Model", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Available Models:[/bold]")
    model_dir = "./models"
    models = [f for f in os.listdir(model_dir) if f.endswith(".gguf")]
    if not models:
        console.print("[bold red]No models found in ./models[/bold red]")
        return None
    for i, model in enumerate(models, 1):
        console.print(f"{i}. {model}")
    console.print("\n[bold]Select a model (1-{len(models)}):[/bold] ", end="")
    choice = Prompt.ask()
    if choice.isdigit() and 1 <= int(choice) <= len(models):
        return os.path.join(model_dir, models[int(choice) - 1])
    return None

def display_config_menu():
    """Display the configuration menu with current settings and options."""
    console.clear()
    title = Text("Configuration", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Current Configuration:[/bold]")
    console.print(f"Thread Fraction: {thread_fraction[0]}/{thread_fraction[1]}")
    console.print(f"Model Temperature: {model_temperature} (0.0-1.0)")
    console.print(f"Audio Volume: {audio_volume} (0.0-1.0)")
    console.print(f"Selected Model: {selected_model}")
    console.print(f"Song Length: {song_length_range[0]}-{song_length_range[1]} minutes" if song_length_range[0] != song_length_range[1] else f"Song Length: {song_length_range[0]} minutes")
    console.print("\n[bold]Options:[/bold]")
    console.print("1. Change Thread Fraction")
    console.print("2. Change Model Temperature")
    console.print("3. Change Audio Volume")
    console.print("4. Select Model")
    console.print("5. Set Song Length")
    console.print("M. Back to Main Menu")
    console.print("\n[bold]Select an option (1-5, M):[/bold] ", end="")
    return Prompt.ask()

def display_main_menu():
    """Display the main menu."""
    console.clear()
    title = Text("LLM Music Generator", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Options:[/bold]")
    console.print("1. Generate Music")
    console.print("2. Configure Options")
    console.print("X. Exit")
    console.print("\n[bold]Select an option (1-2, X):[/bold] ", end="")
    return Prompt.ask()

def get_music_style():
    """Prompt the user to enter a music style."""
    console.print("\n[bold]Enter music style (e.g., jazz, classical, rock):[/bold] ", end="")
    return Prompt.ask()