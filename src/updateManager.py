import configparser
import threading
from time import sleep

from telethon.sync import TelegramClient

from src.Channel import Channel
from src.channelUpdate import channelUpdate

from threading import Thread

config = configparser.ConfigParser()
config.read("Config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
session = config['Telegram']['session']
TelegramClientInstance = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
TelegramClientInstance.start()



def worker(channel):
    if (channelUpdate(channel, TelegramClientInstance)):
        channel.lastDownloadedTimeUpdate()

while True:
    for channel in channelList:
        thread = Thread(target=worker, args=[channel])
        thread.start()

    while threading.active_count() > 1:
        sleep(1)

    sleep(60)
    pull.saveTimestamps()
