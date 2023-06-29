import os
import openai
from services.constants import Constants
from services.capitalize import capitalize_first_letter
from services.read_audio_file import read_audio_file


def speech_to_text(audio_file_path: str) -> str:
    openai.api_key = str(os.getenv("OPENAI_API_KEY"))
    openai.api_base = "https://api.openai.com/v1"
    openai.api_type = "open_ai"
    openai.api_version = None

    audio_file = read_audio_file(audio_file_path)
    print("Audio file processed: ", audio_file_path)
    transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)
    print("Transcript: ", transcript)
    return capitalize_first_letter(transcript.to_dict()["text"])  # type: ignore
