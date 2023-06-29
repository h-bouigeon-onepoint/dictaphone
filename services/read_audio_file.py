import io


def read_audio_file(audio_file_path: str) -> io.BufferedReader:
    return open(audio_file_path, "rb")
