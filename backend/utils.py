# backend/utils.py
import re

def clean_text(text: str) -> str:
    text = re.sub(r"\n+", "\n", text)  # Remove extra newlines
    text = re.sub(r"\s+", " ", text)   # Remove extra spaces
    return text.strip()
