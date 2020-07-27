import os
import eyed3

from src.youtubeSource import downloadLatestFromChannel
from src.utils import *




def changeArtistInMP3File(trackPath, artist):
    audiofile = eyed3.load(trackPath)
    audiofile.tag.artist = artist

    audiofile.tag.save()


def channelUpdate(channel, TelegramClientInstance):

    for youtubeChannelURL in channel.youtubeChannelURLList:

        print("downloading channel {0}, with timestamp {1}".format(youtubeChannelURL, channel.lastDownloadedTime))

        try:
            downloadLatestFromChannel(youtubeChannelURL, channel.lastDownloadedTime)
        except TimeoutError:
            pass
        except:
            print("an error occurred while downloading channel {0}".format(youtubeChannelURL))
            return False

        print("Done downloading")

        path = DEFAULT_DOWNLOAD_PATH + getYouTubeChannelIdFromURL(youtubeChannelURL) + "/"

        print("save path: {0}".format(path))

        try:
            files = os.listdir(path)
        except FileNotFoundError:
            print("Directory {} not found, no files downloaded or bad path".format(path))
            return True

        musicFiles = [file for file in files if file.endswith(".mp3")]


        if len(musicFiles) == 0:
            print("empty music list")
            return True


        for i in musicFiles: changeArtistInMP3File(path + i, channel.telegramChannelName)

        with TelegramClientInstance:
            for musicFile in musicFiles:
                print("uploading {0} to tg chat {1}".format(musicFile, channel.telegramChanelID))

                try:
                    TelegramClientInstance.send_file(channel.telegramChanelID, path + musicFile)
                except:
                    print("not uploaded {0}, keep in folder".format(musicFile))
                    continue

                print("uploaded {0}, removing...".format(musicFile))
                os.remove(path + musicFile)

        print("Uploaded")
        return True





if __name__ == '__main__':
    from src.Channel import Channel

    ch = Channel(["https://www.youtube.com/channel/UCNZq4pkZa4Wk5mHzMLEgO3g"], "sukanz", '20200720')

    import configparser

    from telethon.sync import TelegramClient

    config = configparser.ConfigParser()
    config.read("Config.ini")

    # Присваиваем значения внутренним переменным
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    session = config['Telegram']['session']
    client = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
    client.start()

    channelUpdate(ch, client)

