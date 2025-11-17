import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env if present
load_dotenv()

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


class LLMClient:
    """
    Simple wrapper around the OpenAI client.
    You can swap this out later for Cohere or another provider.
    """

    def __init__(self, model: str = "gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set. Add it to your environment or .env file.")
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, messages: list[dict], temperature: float = 0.2) -> str:
        """
        Send a chat completion request and return the assistant's message content.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()


def parse_json_safely(text: str) -> dict:
    """
    Try to parse JSON from the model response.
    If it fails, wrap it in a helpful structure.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "raw_text": text,
            "error": "Could not parse JSON from model response."
        }


def start_log_session() -> Path:
    """
    Create a new log file for the current support session.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = LOG_DIR / f"session_{timestamp}.log"
    path.touch()
    return path


def append_log(path: Path, content: str) -> None:
    """
    Append a line of text to the session log file.
    """
    with path.open("a", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")

