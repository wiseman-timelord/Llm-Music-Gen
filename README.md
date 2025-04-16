# Llm-Music-Gen
Status: Plan done, on hold (other projects).

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
    Llm-Music-Gen
================================================================================

    1. Begin Generating Music
    2. Configure Options

--------------------------------------------------------------------------------
Selection; Menu Option = 1-2, Exit Program = X:
```
```
================================================================================
    Llm-Music-Gen
================================================================================

Llm-Music-Gen: What kind of music are we making today?
User Input: Dubstep
```
```
================================================================================
    Llm-Music-Gen
================================================================================

Llm-Music-Gen: Making a Dubstep song, time so far: 00:02:15.

[##########--------------------] 33% Complete

--------------------------------------------------------------------------------
```

### Notation
- Sound/Music based Llm's are new to me, so this is partly an experiment; assuming if its text to music, and relys on one prompt, its not going to be as complicated as most of my chatbots.
- Model of interest - [marban/musicgen-large](https://huggingface.co/facebook/musicgen-large).
