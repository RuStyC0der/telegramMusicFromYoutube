import datetime


class Channel():

    def __init__(self, youtubeChannelURLList, telegramChannelID, lastDownloadedTime='20000101', telegramChannelName=' '):

        if type(youtubeChannelURLList) not in (list, tuple):
                raise ValueError('youtubeChannelURLList must be a list or a tuple')

        self.telegramChannelID = telegramChannelID
        self.lastDownloadedTime = lastDownloadedTime
        self.youtubeChannelURLList = youtubeChannelURLList
        self.telegramChannelName = telegramChannelName

    def lastDownloadedTimeUpdate(self, time):
        if time:
            if type(time) != str:
                raise ValueError('must be a string')
            self.lastDownloadedTime = time
        else:
            self.lastDownloadedTime = datetime.datetime.now().strftime('%Y%m%d')

    def __repr__(self):
        return self.telegramChannelID + '/' + self.lastDownloadedTime + '/' + str(self.youtubeChannelURLList) + '/' + self.telegramChannelName


