import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("Config.ini")

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
session = config['Telegram']['session']

client = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
client.start()


# print(client.get_me())
client.send_message('sukanz', 'Hello! Talking to you from Telethon')
client.send_file('sukanz', "/home/unknown/Documents/telegram_api_test/clientAPITest/main.py", caption="123")


# client.send_file
