import src.youtube_dl.youtube_dl as youtube_dl

from src.utils import *




def downloadLatestFromChannel(chanelURL, lastTimeDownloaded, maxDurationInSeconds=None, path=DEFAULT_DOWNLOAD_PATH):

    def match_filter(info_dict):

        # duration in seconds

        # hardcore daterange cutting (stop downloading after first detection)
        date = info_dict.get('upload_date')
        # print("////////////////////////////////")
        # print(date)
        # print(lastTimeDownloaded)
        if date is not None:
            dateRange = youtube_dl.utils.DateRange(lastTimeDownloaded)
            if date not in dateRange:
                print("not in date range")
                raise DateRangeError("not in date range")

        duration = info_dict.get('duration')
        if duration is not None and maxDurationInSeconds is not None:
            if duration > maxDurationInSeconds:
                return "Skipping {0}, because it has not correct duration {1}/{2}".format(info_dict.get('title'), duration, maxDurationInSeconds)

        # print(info_dict)


    # dateRange = youtube_dl.utils.DateRange(lastTimeDownloaded)

    channel_id = getYouTubeChannelIdFromURL(chanelURL)

    ydl_opts = {
        'format': 'bestaudio',
        # 'quiet': True,
        'outtmpl': path + channel_id + "/" + "%(title)s.%(ext)s",
        # 'ignoreerrors' : 'True',
        # 'restrictfilenames' : 'True',
        # 'daterange': dateRange,
        'download_archive': "downloadedLog.log",
        'audio_format': 'mp3',
        'match_filter': match_filter,
        # 'progress_hooks': [_finished_hook],  # func who called after download/conversion
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    ydl.download([chanelURL])




if __name__ == '__main__':
    lastTimeDownloaded = '20000101'


    # def afterDownloadAction(a): pass
    # downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", lastTimeDownloaded, afterDownloadAction)

    downloadLatestFromChannel("https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g", '20210801')
    # downloadLatestFromChannel("https://www.youtube.com/watch?v=Uw2iL6r3NhA", lastTimeDownloaded, 10)
    # ["https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g"], "sukanz", '20210801'

