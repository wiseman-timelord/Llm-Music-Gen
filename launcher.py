# launcher.py
import sys
import os
import time
from rich.console import Console
from rich.progress import Progress
from scripts.interface import display_main_menu, display_config_menu, get_music_style, select_model
from scripts.models import load_model, generate_music
from scripts.utility import text_to_midi, midi_to_audio, play_audio
from scripts.temporary import generation_active, thread_fraction, model_temperature, audio_volume, selected_model, song_length_range, save_config

console = Console()

def main():
    if not os.path.exists("./data"):
        os.makedirs("./data")
    while True:
        choice = display_main_menu()
        if choice == "1":
            style = get_music_style()
            console.print(f"\n[bold]Generating music in {style} style...[/bold]")
            with Progress() as progress:
                task = progress.add_task("[green]Loading model...", total=100)
                model_path = os.path.join("./models", selected_model)
                model = load_model(model_path, thread_fraction[0])
                progress.update(task, advance=50)
                generated_text = generate_music(model, style)
                progress.update(task, advance=25)
                midi_file = text_to_midi(generated_text)
                audio_file = midi_to_audio(midi_file)
                progress.update(task, advance=25)
            console.print("[bold green]Music generated successfully![/bold green]")
            play_audio(audio_file, audio_volume)
        elif choice == "2":
            while True:
                config_choice = display_config_menu()
                if config_choice == "1":
                    console.print("\n[bold]Feature not implemented yet.[/bold]")
                    time.sleep(1)
                elif config_choice == "2":
                    console.print("\n[bold]Feature not implemented yet.[/bold]")
                    time.sleep(1)
                elif config_choice == "3":
                    console.print("\n[bold]Feature not implemented yet.[/bold]")
                    time.sleep(1)
                elif config_choice == "4":
                    new_model = select_model()
                    if new_model:
                        save_config()
                        console.print(f"[bold green]Model changed to {new_model}[/bold green]")
                    else:
                        console.print("[bold red]Model selection cancelled.[/bold red]")
                    time.sleep(1)
                elif config_choice == "5":
                    console.print("\n[bold]Enter song length (e.g., '5' for 5 minutes, '4-6' for 4 to 6 minutes):[/bold] ", end="")
                    length_input = Prompt.ask()
                    try:
                        if '-' in length_input:
                            min_len, max_len = map(float, length_input.split('-'))
                            if min_len > max_len:
                                raise ValueError("Minimum length cannot be greater than maximum length.")
                            song_length_range = [min_len, max_len]
                        else:
                            length = float(length_input)
                            song_length_range = [length, length]
                        if song_length_range[0] <= 0 or song_length_range[1] <= 0:
                            raise ValueError("Song length must be positive.")
                        from scripts.temporary import song_length_range as temp_range
                        temp_range[:] = song_length_range
                        save_config()
                        console.print(f"[bold green]Song length set to {song_length_range[0]}-{song_length_range[1]} minutes[/bold green]" if song_length_range[0] != song_length_range[1] else f"[bold green]Song length set to {song_length_range[0]} minutes[/bold green]")
                    except ValueError as e:
                        console.print(f"[bold red]Invalid input: {e}[/bold red]")
                    time.sleep(1)
                elif config_choice.lower() == "m":
                    break
                else:
                    console.print("[bold red]Invalid option. Please try again.[/bold red]")
                    time.sleep(1)
        elif choice.lower() == "x":
            sys.exit("[bold green]Exiting Llm-Music-Gen.[/bold green]")
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
            time.sleep(1)

def continue_generation():
    from rich.prompt import Prompt
    return Prompt.ask("[bold]Continue generating music? (y/n)[/bold]", choices=["y", "n"], default="y") == "y"

if __name__ == "__main__":
    main()