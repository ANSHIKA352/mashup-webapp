from flask import Flask, render_template, request
from mashup_logic import download_videos, convert_and_trim, merge_audios
import zipfile
import os
import smtplib
from email.message import EmailMessage


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
@app.route("/create", methods=["POST"])
def create():
    singer = request.form["singer"]
    num_videos = int(request.form["videos"])
    duration = int(request.form["duration"])
    email = request.form["email"]

    download_videos(singer, num_videos)
    files = convert_and_trim(duration)
    merge_audios(files, "mashup.mp3")

    with zipfile.ZipFile("mashup.zip", "w") as zipf:
        zipf.write("mashup.mp3")

    send_email(email)

    return "Mashup created and sent to your email!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



def send_email(receiver_email):
    sender_email = "your_email@gmail.com"
    app_password = "your_16_character_app_password"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Your mashup.zip is attached.")

    with open("mashup.zip", "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="zip", filename="mashup.zip")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)




