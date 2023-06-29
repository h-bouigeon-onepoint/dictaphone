import os


def get_file_paths(directories_path: list[str]) -> list[str]:
    file_paths = []
    for directory_path in directories_path:
        file_paths += os.listdir(directory_path)
    file_paths.sort()
    print("All files path in directory: ", file_paths)
    return file_paths


def get_full_file_paths(directory_path: str) -> list[str]:
    file_paths = []
    # use os.walk to recursively traverse the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            # append the full file path to the list
            file_paths.append(os.path.join(dirpath, filename))
    file_paths.sort()
    return file_paths
