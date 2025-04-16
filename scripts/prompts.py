# scripts/prompts.py
import json
from rich.console import Console

console = Console()

# scripts/prompts.py
def load_prompt_template(style):
    return f"Generate music in the style of {style}. Output as comma-separated values: pitch,start,duration,velocity per note."