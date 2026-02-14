import sys
import os
import yt_dlp
from pydub import AudioSegment

DOWNLOAD_FOLDER = "downloads"

def validate_inputs():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("Error: NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("Error: AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    return singer, num_videos, duration, output_file


def download_videos(singer, num_videos):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_query = f"ytsearch{num_videos}:{singer} songs"
            ydl.download([search_query])
    except Exception as e:
        print("Error while downloading videos:", e)
        sys.exit(1)


def convert_and_trim(duration):
    trimmed_files = []
    valid_extensions = (".webm", ".m4a", ".mp4")

    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.lower().endswith(valid_extensions):
            file_path = os.path.join(DOWNLOAD_FOLDER, file)

            audio = AudioSegment.from_file(file_path)
            trimmed_audio = audio[:duration * 1000]

            mp3_name = file_path.replace(".", "_trimmed.") + "mp3"
            trimmed_audio.export(mp3_name, format="mp3")

            trimmed_files.append(mp3_name)

    return trimmed_files




def merge_audios(files, output_file):
    try:
        combined = AudioSegment.empty()

        for file in files:
            audio = AudioSegment.from_mp3(file)
            combined += audio

        combined.export(output_file, format="mp3")

    except Exception as e:
        print("Error merging audios:", e)
        sys.exit(1)


def main():
    singer, num_videos, duration, output_file = validate_inputs()

    print("Downloading videos...")
    download_videos(singer, num_videos)

    print("Converting and trimming...")
    trimmed_files = convert_and_trim(duration)

    print("Merging audio files...")
    merge_audios(trimmed_files, output_file)

    print(f"\nMashup created successfully: {output_file}")


if __name__ == "__main__":
    main()
