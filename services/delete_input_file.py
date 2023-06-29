import os
from services.constants import Constants


def delete_input_file(filename: str) -> None:
    directory = "./"
    files_to_delete_paths = [
        "{upload_path}{filename}".format(
            filename=filename, upload_path=Constants.UPLOADS_PATH
        ),
        "{meeting_report_path}{filename}.json".format(
            filename=filename, meeting_report_path=Constants.MEETING_REPORT_PATH
        ),
        "{transcript_path}{filename}.txt".format(
            filename=filename, transcript_path=Constants.TRANSCRIPT_PATH
        ),
        "{metadata_path}{filename}.pickle".format(
            filename=filename, metadata_path=Constants.METADATA_PATH
        ),
        "{record_path}{filename}".format(
            filename=filename, record_path=Constants.AUDIO_RECORDED_PATH
        ),
        "{compressed_path}{filename}.mp3".format(
            filename=filename, compressed_path=Constants.AUDIO_COMPRESSED_PATH
        ),
    ]

    for path in files_to_delete_paths:
        file_path = os.path.join(directory, path)
        print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file: {path}")
        else:
            print(f"File not found: {path}")
