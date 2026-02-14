# 🎵 YouTube Mashup Generator

This project implements a YouTube Mashup Generator as part of the assignment requirements.

The application performs the following tasks:

- Downloads N videos of a given singer from YouTube
- Converts videos to audio
- Trims the first Y seconds from each audio file
- Merges all trimmed audio files into a single mashup
- Creates a ZIP file of the final output
- Sends the mashup via email (Web version)

---

## 📌 Project Structure

### Program 1 – Command Line Application

File:
<RollNumber>.py


Features:
- Accepts command line arguments
- Validates inputs
- Handles exceptions
- Downloads YouTube videos
- Converts to audio
- Trims audio
- Merges into single MP3 file

### Program 2 – Web Application (Flask)

Files:
- `app.py`
- `mashup_logic.py`
- `templates/index.html`

Features:
- User inputs singer name, number of videos, duration, and email
- Generates mashup
- Creates ZIP file
- Sends ZIP file via email

---

## ⚙️ Requirements

Python Version:
Python 3.11

Required Libraries:
flask
yt-dlp
pydub
moviepy
gunicorn

Install using:

pip install -r requirements.txt


FFmpeg must be installed and added to system PATH.

---

## ▶️ How to Run Program 1 (CLI)

py -3.11 <RollNumber>.py "Singer Name" <NumberOfVideos> <Duration> <OutputFileName>


Example:

py -3.11 102303042.py "Arijit Singh" 11 21 output.mp3


Conditions:
- NumberOfVideos > 10
- Duration > 20 seconds

---

## 🌐 How to Run Program 2 (Web App)

Navigate to project folder:

py -3.11 app.py


Open browser:

http://127.0.0.1:5000


Fill the form and generate mashup.

---

## 📧 Email Configuration

For email functionality:

- Enable 2-Step Verification in Gmail
- Generate App Password
- Set environment variables:

SENDER_EMAIL = your_email@gmail.com
EMAIL_PASSWORD = your_16_character_app_password


---

## ⚠️ Notes

- Application works locally using Python 3.11.
- FFmpeg is required for audio processing.
- Processing time depends on internet speed and number of videos.
- Only audio/video files are processed during conversion.

---

## 🧠 Technologies Used

- Python
- Flask
- yt-dlp
- pydub
- FFmpeg
- smtplib
