from services.handle_json import read_json_file
from services.get_file_paths_in_directory import get_full_file_paths


def get_all_json_contents(directory_path: str) -> list[dict]:
    files_paths = get_full_file_paths(directory_path)
    print("All txt file paths : ", files_paths)
    all_json_contents = []
    for json_path in files_paths:
        all_json_contents.append(read_json_file(json_path))
    return all_json_contents
