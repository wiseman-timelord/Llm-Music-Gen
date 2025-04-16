# scripts/interface.py
from rich.console import Console
from rich.prompt import Prompt, FloatPrompt
from rich.panel import Panel
from rich.text import Text
from scripts.temporary import thread_fraction, model_temperature, audio_volume

console = Console()

def display_main_menu():
    console.clear()
    title = Text("Llm-Music-Gen", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Main Menu[/bold]\n")
    console.print("1. Begin Generating Music")
    console.print("2. Configure Options")
    console.print("X. Exit Program")
    console.print("\n[bold]Select an option (1-2, X):[/bold] ", end="")
    return Prompt.ask()

def display_config_menu():
    console.clear()
    title = Text("Configuration", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Current Configuration:[/bold]")
    console.print(f"Thread Fraction: {thread_fraction[0]}/{thread_fraction[1]}")
    console.print(f"Model Temperature: {model_temperature} (0.0-1.0)")
    console.print(f"Audio Volume: {audio_volume} (0.0-1.0)")
    console.print("\n[bold]Options:[/bold]")
    console.print("1. Change Thread Fraction")
    console.print("2. Change Model Temperature")
    console.print("3. Change Audio Volume")
    console.print("M. Back to Main Menu")
    console.print("\n[bold]Select an option (1-3, M):[/bold] ", end="")
    return Prompt.ask()

def get_music_style():
    console.clear()
    title = Text("Music Generation", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]What kind of music are we making today?[/bold]")
    console.print(" (e.g., jazz, classical, rock)")
    return Prompt.ask()

def configure_thread_fraction():
    console.clear()
    title = Text("Thread Fraction", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Available thread fractions:[/bold]")
    fractions = ["1/2", "2/3", "3/4", "4/5", "5/6", "6/7", "8/9", "9/10", "1/1"]
    for i, frac in enumerate(fractions, 1):
        console.print(f"{i}. {frac}")
    console.print("\n[bold]Select a fraction (1-9, or Enter to cancel):[/bold] ", end="")
    choice = Prompt.ask()
    if choice.isdigit() and 1 <= int(choice) <= 9:
        return tuple(map(int, fractions[int(choice)-1].split("/")))
    return None

def configure_model_temperature():
    console.clear()
    title = Text("Model Temperature", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Enter new temperature (0.0-1.0):[/bold] ", end="")
    return FloatPrompt.ask()

def configure_audio_volume():
    console.clear()
    title = Text("Audio Volume", style="bold cyan", justify="center")
    console.print(Panel(title, expand=False))
    console.print("\n[bold]Enter new volume (0.0-1.0):[/bold] ", end="")
    return FloatPrompt.ask()