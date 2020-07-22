
import ytdlTest.youtube_dl as youtube_dl

import datetime

lastTimeDownloaded = "20190709"

nowDate = datetime.datetime.now().strftime("%Y%m%d")
daterange = youtube_dl.utils.DateRange(lastTimeDownloaded, nowDate)




def finished_hook(d):
    if d['status'] == 'converted':
        print("////////////////////////////////")
        print(d)
        print("////////////////////////////////")
        pass

    # print(d['status'])

ydl_opts = {
        'format' : 'bestaudio',
        'quiet': True,
        'outtmpl' : "./tmpTacksFolder/%(title)s.%(ext)s",
        # 'ignoreerrors' : 'True',
        # 'restrictfilenames' : 'True',
        'daterange' : daterange,
        'audio_format' : 'mp3',
        'progress_hooks' : [finished_hook], # func who called after download
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        }

ydl = youtube_dl.YoutubeDL(ydl_opts)
print(ydl.params)



ydl.download(['https://www.youtube.com/channel/UCPGYY5ZEl6UThPpNGfnd28Q'])



# print(video)

