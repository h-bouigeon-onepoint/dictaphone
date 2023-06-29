import pickle
from typing import Dict


def write_pickle_file(file_path: str, data: Dict) -> None:
    """Write a dictionary to a pickle file.

    Args:
        file_path (str): The path to the pickle file to write.
        data (dict): The dictionary to write to the pickle file.
    """
    with open(file_path, "wb") as file:
        pickle.dump(data, file)


def read_pickle_file(file_path: str) -> Dict:
    """Read a dictionary from a pickle file.

    Args:
        file_path (str): The path to the pickle file to read.

    Returns:
        dict: The dictionary read from the pickle file.
    """
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    return data
