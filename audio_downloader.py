from pytube import YouTube
import os
import pandas as pd
import re


def clean_filename(title):
    # Remove special characters that are not allowed in filenames
    cleaned_title = re.sub(r'[^\w\s.-]', '', title)
    return cleaned_title

def download_audio(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    print(
        f"Downloading video with id = {video_id}")
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio = True).first()
        title = yt.title
        title = clean_filename(title)
        title = title + '.mp3'
        path = os.path.join("downloaded_audios")
        stream.download(path,filename = title)
    except Exception as e:
        print(e)

def main():
    df = pd.read_excel("significant_events.xlsx")

    for video_id in df['Video ID']:
        download_audio(video_id)

if __name__ == '__main__':
    main()