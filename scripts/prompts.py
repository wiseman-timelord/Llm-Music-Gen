# scripts/prompts.py

prompts = {
    "default": "Generate music in the style of {style}. Output as comma-separated values: pitch,start,duration,velocity per note.",
    "jazz": "Generate a jazz piece with improvisational elements. Output as comma-separated values: pitch,start,duration,velocity per note.",
    "classical": "Generate a classical composition reminiscent of the Romantic era. Output as comma-separated values: pitch,start,duration,velocity per note.",
    "rock": "Generate a rock song with a strong rhythm section. Output as comma-separated values: pitch,start,duration,velocity per note."
}

def load_prompt_template(style):
    """Load and format the prompt template for the given music style."""
    return prompts.get(style.lower(), prompts["default"]).format(style=style)