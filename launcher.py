# launcher.py
import sys
from rich.console import Console
from rich.progress import Progress
from scripts.interface import (
    display_main_menu, display_config_menu, get_music_style,
    configure_thread_fraction, configure_model_temperature, configure_audio_volume
)
from scripts.models import load_model, generate_music
from scripts.utility import text_to_midi, midi_to_audio, play_audio
from scripts.temporary import (
    generation_active, thread_fraction, set_thread_fraction,
    set_model_temperature, set_audio_volume
)

console = Console()

def main():
    model_path = "./data/music_generation_model.Q6_K.gguf"
    num_threads = round(24 * thread_fraction[0] / thread_fraction[1])
    model = load_model(model_path, num_threads)

    while True:
        choice = display_main_menu()
        if choice == "1":
            style = get_music_style()
            while generation_active:
                try:
                    with Progress() as progress:
                        task = progress.add_task("[cyan]Processing...", total=100)
                        music_text = generate_music(model, style)
                        console.print(f"[bold yellow]Model output: {music_text}[/bold yellow]")
                        progress.update(task, advance=25)
                        midi_file = text_to_midi(music_text)
                        progress.update(task, advance=25)
                        audio_file = midi_to_audio(midi_file)
                        progress.update(task, advance=25)
                        play_audio(audio_file)
                        progress.update(task, advance=25)
                    if not continue_generation():
                        break
                except Exception as e:
                    if "MIDI" in str(e):
                        console.print("[bold red]Error: Invalid MIDI data generated. Check model output.[/bold red]")
                    elif "audio" in str(e):
                        console.print("[bold red]Error: Audio processing failed. Check dependencies.[/bold red]")
                    else:
                        console.print(f"[bold red]Error: {e}[/bold red]")
        elif choice == "2":
            while True:
                config_choice = display_config_menu()
                if config_choice == "1":
                    new_fraction = configure_thread_fraction()
                    if new_fraction:
                        set_thread_fraction(new_fraction)
                        num_threads = round(24 * thread_fraction[0] / thread_fraction[1])
                        model = load_model(model_path, num_threads)
                elif config_choice == "2":
                    new_temperature = configure_model_temperature()
                    if 0.0 <= new_temperature <= 1.0:
                        set_model_temperature(new_temperature)
                    else:
                        console.print("[bold red]Temperature must be between 0.0 and 1.0.[/bold red]")
                elif config_choice == "3":
                    new_volume = configure_audio_volume()
                    if 0.0 <= new_volume <= 1.0:
                        set_audio_volume(new_volume)
                    else:
                        console.print("[bold red]Volume must be between 0.0 and 1.0.[/bold red]")
                elif config_choice.lower() == "m":
                    break
                else:
                    console.print("[bold red]Invalid choice, try again.[/bold red]")
        elif choice.lower() == "x":
            sys.exit("[bold green]Exiting Llm-Music-Gen.[/bold green]")
        else:
            console.print("[bold red]Invalid choice, try again.[/bold red]")

def continue_generation():
    from rich.prompt import Prompt
    return Prompt.ask("[bold]Continue generating music? (y/n)[/bold]", choices=["y", "n"], default="y") == "y"

if __name__ == "__main__":
    main()