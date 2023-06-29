def read_bytes_file(file_path: str) -> bytes:
    print("File Read :", file_path)
    with open(file_path, "rb") as file:
        text = file.read()
    print("First 5 chars in the bytes file: ", text[0:5])
    return text
