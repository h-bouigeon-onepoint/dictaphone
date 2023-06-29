import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from domain.model.transcript import Transcript
from services.convert_audio_to_mp3 import convert_audio_file_to_mp3


class AudioFile:
    def __init__(self, file: FileStorage, language: str) -> None:
        self.file = file
        self.filename = secure_filename(str(self.file.filename))
        self.filepath = os.path.join(app.config["UPLOAD_FOLDER"], self.filename)
        self.audio_compressed_path = os.path.join(
            app.config["COMPRESSED_AUDIO_FOLDER"], self.filename
        )
        self.language = language
        self.transcript = Transcript(self.filename, self.language)

    def save(self) -> None:
        self.file.save(self.filepath)

    def convert_to_mp3(self) -> None:
        convert_audio_file_to_mp3(
            self.filepath,
            self.audio_compressed_path,
        )
