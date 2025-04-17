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
- While Generating and Converting, workflow is printed...
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
I will be making the program for THESE specific llama based gguf music generation models, total ~11GB, the specific quantizations of the models shown, will be tested, but other quantizations of the same files must also work...
- [ILM3-8B-Ruby-Music-GGUF](https://huggingface.co/mradermacher/ILM3-8B-Ruby-Music-GGUF), example model name `ILM3-8B-Ruby-Music.Q3_K_M.gguf` example case size 4.39 GB...
```
ILM3-8B-Ruby-Music-GGUF
Model Description: This model is based on InternLM3, not LLaMA 3, and is fine-tuned for roleplaying and creative writing. It was trained on a mix of private instruct (1k samples), roleplaying (2.5k human and ~1k synthetic samples), and public datasets, including some related to music (e.g., allura-org/fujin-cleaned-stage-2). It uses ChatML format for input.

Capabilities:
Primarily generates creative text, such as lyrics, stories, or thematic descriptions, suitable for conversational or prompt-based text generation.
Has issues with outputting the EOS token, which can cause rambling, but this can be mitigated with logit bias settings (e.g., setting logit bias for <|im_end|> to 2).
Recommended sampler settings include temp 1, smoothing factor 0.5, smoothing curve 1, and DRY 0.5/1.75/5/1024, though these are for text generation stability.

Role in the Project:
Best used for generating creative text prompts that can be fed into music generation models, enhancing user inputs if they are vague or need more detail (e.g., generating lyrics for "Chill, Dubstep").
Not suitable for direct music generation, as it is focused on text output, but can support the workflow by providing richer prompts.
Hardware Compatibility: Likely compatible with standard hardware, including Windows 10, as it's in GGUF format and designed for consumer GPUs.
```
- [ChatMusician-GGUF](https://huggingface.co/mradermacher/ChatMusician-GGUF) example model name `ChatMusician.Q6_K.gguf`, example case size 5.53 GB...
```
ChatMusician-GGUF
Model Description: An open-source model based on LLaMA2, specifically designed for music generation through text-based conversations, available in GGUF format with various quantization levels.

Capabilities:
Generates well-structured, full-length music conditioned on texts, chords, melodies, motifs, and musical forms, surpassing GPT-4 in 76% of cases and GPT-3.5 in 85% (Reddit Discussion).
Supports multi-turn dialogue and is compatible with clients like llama.cpp, text-generation-webui, and KoboldCpp (ChatMusician-GGUF Dataloop).

Role in the Project: Ideal for music generation from prompts generated by ILM3-8B-Ruby-Music, fitting your GGUF and Windows 10 requirements.
Hardware Compatibility: Designed for standard hardware, including Windows 10, making it accessible.
```

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
