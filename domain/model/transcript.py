import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from services.api.speech_to_text import speech_to_text
from services.handle_txt import read_txt_file, write_txt_file
from domain.model.meeting_report import MeetingReport


class Transcript:
    def __init__(self, filename: str, language: str = "french") -> None:
        self.filename = secure_filename(str(filename))
        self.filepath = os.path.join(app.config["TRANSCRIPT_FOLDER"], self.filename)
        self.audio_compressed_path = os.path.join(
            app.config["COMPRESSED_AUDIO_FOLDER"], self.filename
        )
        self.language = language
        self.content = ""

    def get_transcript_from_audio(self) -> None:
        self.content = speech_to_text(f"{self.audio_compressed_path}.mp3")

    def read_from_txt(self) -> None:
        self.content = read_txt_file(f"{self.filepath}.txt")

    def write_to_txt(self) -> None:
        write_txt_file(
            f"{self.filepath}.txt",
            self.content,
        )

    def create_meeting_report(self, language: str = "french") -> None:
        self.meeting_report = MeetingReport(self.filename, self.content, language)
        self.meeting_report.get_meeting_report_from_transcript()
        self.meeting_report.write_to_json()
