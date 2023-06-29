from pydub import AudioSegment


def convert_audio_file_to_mp3(audio_file_path: str, output_path: str) -> None:
    sound = AudioSegment.from_file(audio_file_path)
    sound.export(f"{output_path}.mp3", format="mp3")
