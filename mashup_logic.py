import os
import yt_dlp
from pydub import AudioSegment

DOWNLOAD_FOLDER = "downloads"

def download_videos(singer, num_videos):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        'format': 'worstaudio',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch{num_videos}:{singer} songs"
        ydl.download([search_query])


def convert_and_trim(duration):
    trimmed_files = []
    valid_extensions = (".webm", ".m4a", ".mp4")

    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.lower().endswith(valid_extensions):

            file_path = os.path.join(DOWNLOAD_FOLDER, file)

            audio = AudioSegment.from_file(file_path)
            trimmed_audio = audio[:duration * 1000]

            mp3_name = file_path + ".mp3"
            trimmed_audio.export(mp3_name, format="mp3")

            trimmed_files.append(mp3_name)

    return trimmed_files


def merge_audios(files, output_file):
    combined = AudioSegment.empty()

    for file in files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    combined.export(output_file, format="mp3")
