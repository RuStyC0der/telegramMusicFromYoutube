#!/bin/bash

installPath=/usr/local/
downloadDirectory="telegramMusicFromYoutube"

pythonPath=$(command -v python3)

echo $pythonPath

cd $installPath

echo "Check if python3 is installed..."

if [ ! -z "$pythonPath" ]
then
echo "OK"
else
echo "ERROR: python3 is not installed!"
echo "Please install python and re-run this script again"
exit 1
fi

echo "Download lasest version to $downloadDirectory..."

if ! git clone https://github.com/RuStyC0der/telegramMusicFromYoutube/tree/master $downloadDirectory
then
    echo "Failed to clone... exit"
    exit 1
fi

cd $downloadDirectory



echo "Install requirements..."

if ! $pythonPath -m pip install -r requirements.txt
then
echo "Failed to install requirements... exit"
exit 1
fi











serviceBody="
[Unit]
Description=From youtube to telegram upload daemon

[Service]
WorkingDirectory=$(pwd)
ExecStart=$pythonPath -m src.UpdateManager
Restart=always

[Install]
WantedBy=multi-user.target 
"

echo "$serviceBody"

