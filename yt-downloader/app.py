from pytube import YouTube
import os
import pandas as pd
import random


def download_video(video_list, resolution, path):
    for video in video_list:
        url = f"https://www.youtube.com/watch?v={video['VideoId']}"
        print(
            f"Downloading {video['VideoId']}_{video['Channel']}_{video['ShowName']}")
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(
                res=resolution, progressive=True).first()
            stream.download(output_path=os.path.join(path, f"{yt.title}.mp4"))
        except Exception as e:
            print(e)


def read_data(path, filename, sheet):
    try:
        video_links = pd.read_excel(
            os.path.join(path, filename), sheet_name=sheet)
    except FileNotFoundError as fnf:
        print(f'File not found at {os.path.join(path, filename)}.')
    except Exception as e:
        print(f'Problem with reading {filename} file.')
    return video_links


def overview(consolidated_video_links):
    unique_channels_shows = consolidated_video_links.filter(['Channel', 'ShowName', 'VideoId']).groupby(
        ['Channel', 'ShowName']).agg(video_count=('VideoId', 'count'))
    channels_showname = list(zip(*unique_channels_shows.index))
    print(f'\n******* Data Overview *******\nNumber of prime-time videos for each Channel-Show combination:\n{unique_channels_shows}\n\n' +
          f'Unique Channels\' List:\n{set(channels_showname[0])}\n\nUnique Shows\' List:\n{set(channels_showname[1])}\n\n' +
          f'Number of Hindi and English debates respectively:\n{consolidated_video_links["language"].value_counts()}\n\n')


def main():
    PATH = '.'
    ENG_LINKS_FILENAME = 'English_channels_videos.xlsx'
    ENG_LINKS_SHEET = 'Sheet1'
    HIND_LINKS_FILENAME = 'Hindi_channel_videos.xlsx'
    HIND_LINKS_SHEET = 'Sheet1'
    OUTPUT_PATH = 'downloaded_videos'
    RESOLUTION = '360p'
    if not os.path.exists(os.path.join(PATH, OUTPUT_PATH)):
        os.mkdir(os.path.join(PATH, OUTPUT_PATH))
    else:
        pass
    eng_video_links = read_data(
        path=PATH, filename=ENG_LINKS_FILENAME, sheet=ENG_LINKS_SHEET)
    eng_video_links['language'] = 'english'
    hind_video_links = read_data(
        path=PATH, filename=HIND_LINKS_FILENAME, sheet=HIND_LINKS_SHEET)
    hind_video_links['language'] = 'hindi'
    consolidated_video_links = pd.concat(
        [eng_video_links, hind_video_links], axis=0, ignore_index=True)
    consolidated_video_links.reset_index(inplace=True)

    # overview(consolidated_video_links)

    random.seed(1000)
    video_list = []
    for channel in set(consolidated_video_links['Channel']):
        subset = consolidated_video_links.loc[consolidated_video_links['Channel'] == channel, :]
        random_video = subset.iloc[random.choice(range(subset.shape[0])), :]
        video_list.append(random_video)

    print('\n******* Download Started *******')
    download_video(video_list=video_list, resolution=RESOLUTION,
                   path=os.path.join(PATH, OUTPUT_PATH))
    print('\n******* Download Ended *******')


if __name__ == '__main__':
    main()
