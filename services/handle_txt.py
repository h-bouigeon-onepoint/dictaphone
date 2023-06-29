def read_txt_file(txt_file_path: str) -> str:
    print("File Read :", txt_file_path)
    with open(txt_file_path, "r") as file:
        text = file.read()
    print("Preview: ", text[0:5])
    return text


def write_txt_file(filename: str, text: str) -> None:
    print("File written : ", filename)
    file = open(filename, "w")
    file.write(text)
    file.close()
    print("File successfully written.")
