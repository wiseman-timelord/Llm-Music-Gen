# Llm-Music-Gen
Status: Planning

### Project Goals
- Modular Design: Create a maintainable and scalable codebase with clear separation of concerns.
- User Experience: Provide an intuitive text-based interface for seamless interaction.
- Music Generation: Leverage LLMs and music generation libraries to produce music in various styles.
- Automation: Implement a loop for continuous music generation with an option to cancel.
- Compatibility: Ensure the application runs smoothly on Ubuntu 24.10.

### File Structure
```
./Llm-Music-Gen.sh: Launcher/installer script.
./main_script.py: Main application script.
./data/prompt.txt: Template for prompts sent to the LLM.
./scripts/models.py: Handles interactions with the LLM.
./scripts/utility.py: Backend utilities and helper functions.
./scripts/interface.py: Manages text interface, menus, and prompts.
```

### Technology Stack and Dependencies
- Programming Language: Python 3.10 or higher.
- LLMs and Libraries: OpenAI's GPT-4 (if accessible) or open-source alternatives like Hugging Face Transformers.Music generation libraries such as Magenta by TensorFlow or MuseNet.
- Audio Processing: Pydub for audio manipulation. Simpleaudio or Playsound for audio playback.
- User Interface: Python's built-in curses library for advanced text-based UI (optional).
- Shell Scripting: Bash for the launcher/installer script.

### Description
Llm-Music-Gen is a command-line Python application designed to generate music based on user-defined styles using Large Language Models (LLMs). The program provides a user-friendly interface with options to configure music styles, generate music, and play the generated tracks automatically.
