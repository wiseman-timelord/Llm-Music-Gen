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

1. Change Thread Fraction (5/6)

2. Change Model Temperature (0.75)

3. Change Audio Volume (65%)

4. Select Model (**modelnameShortenedTo20Characters**)

5. Set Song Length (5 Minutes)

6. Auto-Play After Convert (true)

================================================================================
Selection; Options = 1-6, Back to Menu = B:
```

### Models
I will be making the program for THESE llama based gguf music generation models...
- `ILM3-8B-Ruby-Music-GGUF`, in my case `ILM3-8B-Ruby-Music.Q6_K.gguf`
- `ScrapeGoat-Music-Stage2-GGUF`, in my case `ScrapeGoat-Music-Stage2.Q6_K.gguf`
- `music_generation_model-GGUF`, in my case `music_generation_model.Q6_K.gguf`

### Development
- Working on...
```
- verifying the token-to-minute mapping.
- ensuring ffmpeg is installed for MP3 conversion. Mp3 
- enhancing multi-model support. Unsure if this means using models together, or just model support. If just support then we are only supporting llama models such as specifically the three models mentioned though quantization depth should obviously be supported, ie not limited by those specific file names.
- improving progress bar granularity. 
- considering multi-track MIDI support.
- ensure menus are in-line with the previews provided.
```
- Afterwards...
```
- The program should continue to make normal lengh songs of minutes but I want such options on the main page not configuration page, and also  I would like to be able to specify on Main page frequencies, so as to be able to make music at a specific frequency, like those meditation songs on youtube. If we can generate some awesome music at sacred frequencies, that would go on for 1, 2, 4, 8, hours, then upload to youtube with some visuals I make in another program, then we have likes and subscribbles.. 
- time should be able to be specified as, for example, `HH:MM`, `M`, `M-M`.
```
