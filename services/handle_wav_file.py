import wave


class WavWriter:
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.sample_rate = 44100
        self.wav_file = wave.open(self.audio_file_path, "wb")
        self.wav_file.setnchannels(1)  # mono audio
        self.wav_file.setsampwidth(2)  # 16-bit audio
        self.wav_file.setframerate(self.sample_rate)

    def write_audio(self, audio_data):
        self.wav_file.writeframes(audio_data)

    def close(self):
        self.wav_file.close()
