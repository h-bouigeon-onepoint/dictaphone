from flask import (
    Flask,
    request,
    send_from_directory,
    render_template,
    redirect,
    url_for,
    send_file,
)
import os
from services.constants import Constants
from services.delete_input_file import delete_input_file
from services.send_file import send_word_file, send_ppt_file
from services.get_all_txt_contents import get_all_txt_contents
from services.get_all_json_contents import get_all_json_contents
from services.get_file_paths_in_directory import get_file_paths
from domain.model.audio_file import AudioFile
from domain.model.transcript import Transcript
from domain.model.meeting_report import MeetingReport


app = Flask(__name__)
app.config["COMPRESSED_AUDIO_FOLDER"] = Constants.AUDIO_COMPRESSED_PATH
app.config["MEETING_REPORT_FOLDER"] = Constants.MEETING_REPORT_PATH
app.config["TRANSCRIPT_FOLDER"] = Constants.TRANSCRIPT_PATH
app.config["RECORD_FOLDER"] = Constants.AUDIO_RECORDED_PATH
app.config["METADATA_FOLDER"] = Constants.METADATA_PATH
app.config["UPLOAD_FOLDER"] = Constants.UPLOADS_PATH
app.config["PPT_FOLDER"] = Constants.METADATA_PATH
app.config["WORD_FOLDER"] = Constants.WORD_PATH
app.config["PPT_FOLDER"] = Constants.PPT_PATH


@app.route("/index")
@app.route("/")
def index():
    audio_filenames = get_file_paths(
        [app.config["UPLOAD_FOLDER"], app.config["RECORD_FOLDER"]]
    )
    transcripts_content = get_all_txt_contents(app.config["TRANSCRIPT_FOLDER"])
    meeting_reports_content = get_all_json_contents(app.config["MEETING_REPORT_FOLDER"])
    file_count = len(audio_filenames)

    return render_template(
        "index.html",
        transcripts=transcripts_content,
        meeting_reports=meeting_reports_content,
        audio_filenames=audio_filenames,
        file_count=file_count,
    )


@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    print(filename)
    delete_input_file(filename)
    return redirect(url_for("index"))


@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    uploaded_filename = str(uploaded_file.filename)  # type:ignore
    language = str(request.form["language"])

    if not uploaded_file or (
        uploaded_filename[-4:] not in Constants.AUDIO_FILE_FORMATS_SUPPORTED
        and uploaded_filename[-5:] not in Constants.AUDIO_FILE_FORMATS_SUPPORTED
    ):
        return render_template("no_file_uploaded.html")

    try:
        audio_file = AudioFile(uploaded_file, language)
        audio_file.save()
        audio_file.convert_to_mp3()
        audio_file.transcript.get_transcript_from_audio()
        audio_file.transcript.write_to_txt()
        audio_file.transcript.create_meeting_report(language)
        audio_file.transcript.meeting_report.write_metadata_to_pickle()
    except Exception as error:
        print("EXCEPTION ERROR : ")
        print(type(error))  # the exception type
        print(error.args)  # arguments stored in .args
        print(error)
        delete_input_file(uploaded_filename)
        return render_template("error_page.html", error=error)

    return redirect(url_for("index"))


@app.route("/recomputeMeetingReport/<filename>", methods=["POST"])
def recomputeMeetingReport(filename):
    audio_filename = str(filename)
    language = str(request.form["language"])

    if not audio_filename:
        return "No filename given or filename incorrect.", 400

    transcript = Transcript(audio_filename, language)
    transcript.read_from_txt()
    transcript.create_meeting_report(language)
    transcript.meeting_report.write_metadata_to_pickle()
    return redirect(url_for("index"))


@app.route("/downloadMeetingReportToWord/<filename>", methods=["POST"])
def downloadMeetingReportToWord(filename):
    meeting_report = MeetingReport(filename)
    meeting_report.read_from_json()
    meeting_report.write_to_word()
    return send_word_file(meeting_report.get_word_file())


@app.route("/downloadMeetingReportToPpt/<filename>", methods=["POST"])
def downloadMeetingReportToPpt(filename):
    meeting_report = MeetingReport(filename)
    meeting_report.read_from_json()
    meeting_report.read_metadata_from_pickle()
    print("Download Ppt in ", meeting_report.language)
    meeting_report.write_to_ppt()
    return send_ppt_file(meeting_report.get_ppt_file())


@app.route("/downloadRecording/<filename>", methods=["POST"])
def downloadRecording(filename):
    return send_file(
        os.path.join(app.config["UPLOAD_FOLDER"], filename), as_attachment=True
    )


@app.route("/audioFile/<filename>")
def audioFile(filename):
    print("audioFile asked =", filename)
    if os.path.exists(os.path.join(app.config["UPLOAD_FOLDER"], filename)):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    return send_from_directory(app.config["RECORD_FOLDER"], filename)


@app.route("/transcript/<filename>")
def transcript(filename):
    print("Transcript audio file path : ")
    print(filename)
    return send_from_directory(app.config["TRANSCRIPT_FOLDER"], filename)


@app.route("/resume/<filename>")
def resume(filename):
    print("Resume audio file path : ")
    print(filename)
    return send_from_directory(app.config["MEETING_REPORT_FOLDER"], filename)


@app.route("/explanatoryNote.html")
def explanatoryNote():
    return render_template("explanatory_note.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/img"), "logo_dictaphone.png"
    )


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=8000)
