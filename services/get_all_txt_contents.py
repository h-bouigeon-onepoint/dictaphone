from services.handle_txt import read_txt_file
from services.get_file_paths_in_directory import get_full_file_paths


def get_all_txt_contents(directory_path: str) -> list[str]:
    files_paths = get_full_file_paths(directory_path)
    print("All txt file paths : ", files_paths)
    all_txt_contents = []
    for txt_path in files_paths:
        all_txt_contents.append(read_txt_file(txt_path))
    return all_txt_contents
