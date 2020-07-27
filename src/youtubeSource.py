import src.youtube_dl as youtube_dl

from src.utils import *

def downloadLatestFromChannel(chanelURL, lastTimeDownloaded, path=DEFAULT_DOWNLOAD_PATH):

    # def _finished_hook(d):
    #     if d['status'] == 'converted':
    #         if afterDownloadAction(d):
    #             pass
    #             # remove file
    #         else:
    #             pass
    #             #

    dateRange = youtube_dl.utils.DateRange(lastTimeDownloaded)

    channel_id = getYouTubeChannelIdFromURL(chanelURL)

    ydl_opts = {
        'format': 'bestaudio',
        # 'quiet': True,
        'outtmpl': path + channel_id + "/" + "%(title)s.%(ext)s",
        # 'ignoreerrors' : 'True',
        # 'restrictfilenames' : 'True',
        'daterange': dateRange,
        'download_archive': "downloadedLog.log",
        'audio_format': 'mp3',
        # 'progress_hooks': [_finished_hook],  # func who called after download/conversion
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    try:
        ydl.download([chanelURL])
    except TimeoutError:
        print("may be daterange limit, if something not working, try to find error here")



if __name__ == '__main__':
    lastTimeDownloaded = '20000101'


    # def afterDownloadAction(a): pass
    # downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", lastTimeDownloaded, afterDownloadAction)

    downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", lastTimeDownloaded)
