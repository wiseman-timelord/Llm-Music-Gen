# Llm-Music-Gen
Status: Alpha (not tested yet, still implementing)

### Project Goals
- Modular Design: Create a maintainable and scalable codebase with clear separation of concerns.
- User Experience: Provide an intuitive text-based interface for seamless interaction.
- Music Generation: Leverage LLMs and music generation libraries to produce music in various styles.
- Automation: Implement a loop for continuous music generation with an option to cancel.
- Compatibility: Ensure the application runs smoothly on Windows 10.

### File Structure
```
./Llm-Music-Gen.bat: Launcher.
./launcher.py: Main application script.
./requisites.py: Installer script, for libraries and json. 
./data/persistent.json: Template for prompts sent to the LLM.
./scripts/models.py: Handles interactions with the LLM.
./scripts/utility.py: Backend utilities and helper functions.
./scripts/interface.py: Manages text interface, menus, and prompts.
./scripts/prompts.py: Templates for prompts sent to the LLM.
./scripts/temporary.py: File with ALL, Global variables, Maps, Lists, those kinds of things (there should be no globals at the tops of any of the scripts, unless we specifically require them to be there).
```

### Technology Stack and Dependencies
- Programming Language: Python 3.10 or higher.
- LLMs on Hugging Face in GGUF format.
- Audio Processing: Pydub for audio manipulation. Simpleaudio or Playsound for audio playback.
- User Interface: Python's built-in curses library for advanced text-based UI (optional).
- Windows Command Shell Scripting: Batch for the launcher/installer menu.

### Description
Llm-Music-Gen is a command-line Python application designed to generate music based on user-defined styles using Large Language Models (LLMs). The program provides a user-friendly interface with options to configure music styles, generate music, and play the generated tracks automatically.
Preview

### Preview
```

================================================================================
    Llm-Music-Gen: Main Menu
================================================================================

Song Length: 4-6 minutes
Selected Model: music_generation_model.Q6_K.gguf

--------------------------------------------------------------------------------

Total Songs Length: HH:MM:SS
Outputted Songs: **NextSongName**, **NextSongName**, **NextSongName**, **NextSongName**, **NextSongName**

--------------------------------------------------------------------------------

    1. Generate Music
    2. Output Jukebox
    3. Configure Options

================================================================================
Selection; Menu Option = 1-3, Refresh Screen = R, Exit Program = X:
```

```
================================================================================
    Llm-Music-Gen: Generate Music
================================================================================

Llm-Music-Gen: What kind of music are we making today? (Styles, separated, by, commas)
User Input: Chill, Dubstep
Llm-Music-Gen: How many songs should I generate?
User Input: 3
Llm-Music-Gen: Producing "Chill, Dubstep" themed song number 1...
[##############################] 100% Complete
Llm-Music-Gen: Converting song number 1 from **format used** to Mp3...
[##########--------------------] 33% Complete

```
- While playing the created Mp3s in Jukebox mode, Having the option to break-out of the playing mp3 loop and return to main or exit...
```
================================================================================
    Llm-Music-Gen: Output Jukebox
================================================================================

Songs Played: **PreviousSongName**, **PreviousSongName**

--------------------------------------------------------------------------------

Playing song: **SongName**
[##########--------------------] MM:SS/MM:SS

--------------------------------------------------------------------------------

Remaining Songs: **NextSongName**, **NextSongName**, **NextSongName**, **NextSongName**, **NextSongName**

================================================================================
Selection; Back to Main = B, Exit Program = X:
```
- Configuration menu...
```
================================================================================
    Llm-Music-Gen: Configuration
================================================================================

Thread Fraction: 5/6
Model Temperature: 0.7 (0.0-1.0)
Audio Volume: 1.0 (0.0-1.0)
Selected Model: music_generation_model.Q6_K.gguf
Song Length: 4-6 minutes

--------------------------------------------------------------------------------

1. Change Thread Fraction
2. Change Model Temperature
3. Change Audio Volume
4. Select Model
5. Set Song Length

================================================================================
Select an option (1-5, M):
```

### Models
I will be making the program for THESE llama based gguf music generation models...
- `ILM3-8B-Ruby-Music-GGUF`, in my case `ILM3-8B-Ruby-Music.Q6_K.gguf`
- `ScrapeGoat-Music-Stage2-GGUF`, in my case `ScrapeGoat-Music-Stage2.Q6_K.gguf`
- `music_generation_model-GGUF`, in my case `music_generation_model.Q6_K.gguf`

### Development
- verifying the token-to-minute mapping.
- ensuring ffmpeg is installed for MP3 conversion.
- enhancing multi-model support.
- improving progress bar granularity. 
- considering multi-track MIDI support.
