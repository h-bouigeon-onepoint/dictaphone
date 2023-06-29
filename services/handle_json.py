import json


def read_json_file(json_file_path: str) -> dict:
    print("Json file read :", json_file_path)
    with open(json_file_path, "r") as file:
        json_file = json.load(file)
    return json_file


def write_json_file(filename: str, data_json: dict) -> None:
    print("File written : ", filename)
    with open(filename, "w") as outfile:
        json.dump(data_json, outfile)
    print("Json file successfully written.")
