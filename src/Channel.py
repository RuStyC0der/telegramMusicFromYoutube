import datetime
import json


class Channel():


    def __init__(self, filename):

        self.filename = filename
        self.__load()


    def lastDownloadedTimeUpdate(self, time=None):
        if time:
            if type(time) != str:
                raise ValueError('must be a string')
            self._channelConfig['lastDownloadedTime'] = time
        else:
            self._channelConfig['lastDownloadedTime'] = datetime.datetime.now().strftime('%Y%m%d')




    def __load(self, ):

        with open(self.filename, 'r') as f:
            configDict = json.load(f)

        if type(configDict['youtubeChannelURLList']) not in (list, tuple):
            raise ValueError('youtubeChannelURLList must be a list or a tuple')

        if 'telegramChannelID' not in configDict:
            raise ValueError('required parapeter telegramChannelID not be configured')
        if 'lastDownloadedTime' not in configDict:
            raise ValueError('required parapeter lastDownloadedTime not be configured')
        if 'youtubeChannelURLList' not in configDict:
            raise ValueError('required parapeter youtubeChannelURLList not be configured')
        if 'trackSign' not in configDict:
            raise ValueError('required parapeter telegramChannelName not be configured')

        self._channelConfig = configDict

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self._channelConfig, f)

    def getYouTubeChannelList(self):
        return self._channelConfig['youtubeChannelURLList']

    def getLastDownloadedTime(self):
        return self._channelConfig['lastDownloadedTime']

    def getTrackSign(self):
        return self._channelConfig['trackSign']

    def getTelegramChanelID(self):
        return self._channelConfig['telegramChannelID']

    def __repr__(self):
        return self._channelConfig['telegramChannelID'] + '/-/' \
               + self._channelConfig['lastDownloadedTime'] + '/-/'\
               + str(self._channelConfig['youtubeChannelURLList']) \
               + '/-/' + self._channelConfig['trackSign']


if __name__ == '__main__':
    pass
    a = Channel("./channelConfig/typeBeatParadise.json")
    print(a)
    a.lastDownloadedTimeUpdate()
    a.save()
    print(a)