import pickle


class ChannelPull():
    def __init__(self, channelList=None, dumpFilename="channelDump"):

        if channelList is None:
            channelList = []

        self.channelList = channelList
        self.dumpFilename = dumpFilename



    def save(self):
        pickle.dump(self.channelList, open(self.dumpFilename, 'wb'))

    def load(self):

        channellistLoaded = pickle.load(open(self.dumpFilename, 'rb'))

        channellistLoaded = self._generateDictFromChannelList(channellistLoaded)

        channelDict = self._generateDictFromChannelList(self.channelList)

        channelDict.update(channellistLoaded)

        self.channelList = list(channelDict.values())


    @staticmethod
    def _generateDictFromChannelList(channelList):
        return {channel.telegramChannelID:channel for channel in channelList}

    def getChannelListCopy(self):
        return self.channelList.copy()

    def getChannelListForWrite(self):
        return self.channelList