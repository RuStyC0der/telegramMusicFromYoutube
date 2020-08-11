import os

import eyed3

maxDurationInSeconds = 720

pathFile = open("./files", "r")

paths = pathFile.readlines()

musicFiles  = [i for i in paths if i.endswith(".mp3")]

for file in musicFiles:
    audiofile = eyed3.load(file)
    duration = audiofile.info.time_secs
    if (duration > maxDurationInSeconds):
        print(f"removing file with duration {duration} seconds")
        os.remove(file)