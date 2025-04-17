# scripts/utility.py
import pretty_midi
import pydub
import simpleaudio
import os
import uuid
import msvcrt
import time
from rich.console import Console
from scripts.temporary import audio_volume

console = Console()

def text_to_midi(music_text):
    """
    Converts text representation of music notes into a MIDI file.

    Args:
        music_text (str): Notes in format "pitch,start,duration,velocity" per line.

    Returns:
        str: Path to the generated MIDI file.

    Raises:
        ValueError: If the text format or values are invalid.
    """
    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0)  # Piano
    try:
        for line in music_text.splitlines():
            if line.strip():
                parts = line.split(",")
                if len(parts) != 4:
                    raise ValueError(f"Invalid MIDI format: {line}")
                pitch, start, duration, velocity = map(float, parts)
                if not (0 <= pitch <= 127 and 0 <= velocity <= 127):
                    raise ValueError(f"Pitch or velocity out of range: {line}")
                if start < 0 or duration <= 0:
                    raise ValueError(f"Invalid start or duration: {line}")
                note = pretty_midi.Note(
                    velocity=int(velocity), pitch=int(pitch),
                    start=start, end=start + duration
                )
                instrument.notes.append(note)
        midi.instruments.append(instrument)
        midi_file = f"./data/raw/{uuid.uuid4()}.midi"
        midi.write(midi_file)
        return midi_file
    except Exception as e:
        console.print(f"[bold red]MIDI Error: {e}[/bold red]")
        raise

def midi_to_audio(midi_file):
    try:
        midi = pretty_midi.PrettyMIDI(midi_file)
        audio_data = midi.synthesize(fs=44100)
        audio = pydub.AudioSegment(
            audio_data.tobytes(), frame_rate=44100, sample_width=2, channels=1
        )
        wav_file = f"./data/raw/{uuid.uuid4()}.wav"
        mp3_file = f"./Output/{uuid.uuid4()}.mp3"
        audio = audio + (20 * audio_volume - 20)  # Volume adjustment
        audio.export(wav_file, format="wav")
        audio.export(mp3_file, format="mp3")
        return wav_file
    except Exception as e:
        console.print(f"[bold red]Error converting MIDI to audio: {e}[/bold red]")
        raise

def play_audio(audio_file):
    try:
        audio = pydub.AudioSegment.from_file(audio_file)
        raw_data = audio.raw_data
        play_obj = simpleaudio.play_buffer(
            raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate
        )
        console.print("[bold]Press 's' to stop playback...[/bold]")
        while play_obj.is_playing():
            if msvcrt.kbhit():
                key = msvcrt.getch().decode()
                if key.lower() == 's':
                    play_obj.stop()
                    break
            time.sleep(0.1)
    except Exception as e:
        console.print(f"[bold red]Error playing audio: {e}[/bold red]")
        raise