from flask import Response


def send_word_file(file: bytes, filename: str = "CR_réunion.docx") -> Response:
    response = Response(
        file,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    response.headers.set("Content-Disposition", "attachment", filename=filename)
    return response


def send_ppt_file(file: bytes, filename: str = "compte_rendu_réunion.pptx") -> Response:
    response = Response(
        file,
        mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
    response.headers.set("Content-Disposition", "attachment", filename=filename)
    return response
