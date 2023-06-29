class Constants:
    AUDIO_FILE_FORMATS_SUPPORTED = [
        ".wav",
        ".mp3",
        ".m4a",
        ".webm",
        ".mp4",
        ".mpga",
        ".mpeg",
    ]

    TRANSCRIPT_PATH = "./data/transcript/"

    RESUME_PATH = "./data/resume/"

    MEETING_REPORT_PATH = "./data/meeting_report/"

    UPLOADS_PATH = "./data/upload/"

    AUDIO_COMPRESSED_PATH = "./data/audio/"

    AUDIO_RECORDED_PATH = "./data/record/"

    WORD_PATH = "./data/export/word/"

    PPT_PATH = "./data/export/ppt/"

    METADATA_PATH = "./data/metadata/"

    TEMPLATE_PPT_PATH = "./data/template/Compte_rendu_réunion.pptx"

    MODEL_JSON_MEETING_REPORT = {
        "title_meeting": "",
        "participants": [str],
        "agenda": [str],
        "elements_discussed": [str],
        "action_to_be_taken": [{"action": "", "responsable": "", "deadline": ""}],
        "notes": "",
    }

    MEETING_REPORT_PROMPT = (
        "Your task is to perform a meeting report, summarize the text delimited by triple backticks "
        "and identify and sum up the following elements :\n"
        "Title's Meeting : Choose a title's meeting\n"
        "Participants: Extract all names of the participant\n"
        "if no participant found, just output an empty list.\n"
        "Agenda: Concise list (maximum 5 elements) of important topics / items on the agenda\n"
        "Elements discussed: Concise list (maximum 5 elements) of the subjects / elements discussed\n"
        "Actions te be taken: A short list (maximum 4 elements) containing dictionnaries of action(s) to be taken and the responsable "
        'and the deadline as follow {{"action":"action", "responsable":"name", "deadline":"date mentioned"}} '
        "if no action to be taken found, just output an empty list.\n"
        "Notes: Make a short summary of the general mood and decisions.\n"
        "Provide them in JSON format with the following keys:\n"
        "title_meeting: str, participants: list, agenda: list, elements_discussed: list, action_to_be_taken: list[dict], notes: str.\n"
        "Only use this format, in {language}, nothing else, be precise, synthetic and DO NOT make up subjects, avoid redundancy.\n"
        "Text: ```{text}```"
    )

    MEETING_REPORT_REFINE_PROMPT = (
        "Your job is to produce a final meeting report\n"
        "We have provided an existing meeting report in JSON format which may be incomplete: {existing_answer}\n"
        "We have the opportunity to refine the existing meeting report\n"
        "For instance, if you find new participant names add them to the Participants list\n"
        "if no participants found, just output an empty list.\n"
        "if you find new Item on the Agenda, combine it with an existing element or add a new element in the agenda list\n"
        "if you find a new Element Discussed, combine it with an existing element or add a new element in the elements_discussed list\n"
        "or a new Action to be taken, combine it with an existing element or add a new element in the action_to_be_taken list "
        'with the following format {{"action":"action", "responsable":"name", "deadline":"date mentioned"}}\n'
        "Write a new foot notes which is a short summary (maximum 3 sentences or 300 characters) of the general mood and decisions using the previous foot notes if necessary\n"
        "(Do it only if needed) with some more context below.\n"
        "------------\n"
        "{text}\n"
        "------------\n"
        "Given the new context, refine the original meeting report but keep the same following output format:\n"
        "title_meeting: str, participants: list, agenda: list (maximum 5 elements), elements_discussed: list (maximum 5 elements), action_to_be_taken: list[dict] (maximum 4 elements), notes: str (maximum 3 sentences or 300 characters).\n"
        "Be aware that the full JSON length must be maximum 950 tokens.\n"
        "If the new context isn't useful, return the original JSON format meeting report."
    )
