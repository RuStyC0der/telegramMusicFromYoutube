#!/bin/bash

installPath=/usr/local/
serviceFilePath=/etc/systemd/system
logPath=/var/log/telegramMusicFromYoutube.log

downloadDirectoryName="telegramMusicFromYoutube"
downloadedLogFileName="downloaded.log"
configFileName="Config.ini"

scriptPath=$(pwd)
pythonPath=$(command -v python3)

echo "Please place your Config.ini and downloaded.log to this folder if you want to copy it to service or copy it manually"
echo "Config.ini example:
[Telegram]
api_id = xxxxxxx
api_hash = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
session = someSessionName
"
echo "Sleep 3sec time to stop the script if you forget to place config file"
sleep 3



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


echo "Download lasest version to $downloadDirectoryName..."
if ! git clone https://github.com/RuStyC0der/telegramMusicFromYoutube/tree/liteVersion $downloadDirectoryName
then
    echo "Failed to clone... exit"
    exit 1
fi
cd $downloadDirectoryName




echo "Install requirements..."
if ! $pythonPath -m pip install -r requirements.txt
then
echo "Failed to install requirements... exit"
exit 1
fi


echo "moving Config..."
if test -f $scriptPath/$configFileName
then
cp $scriptPath/$configFileName ./
else
echo "Config Not Found!"
echo "moving download log..."
if test -f $scriptPath/$downloadedLogFileName
then
cp $scriptPath/$downloadedLogFileName ./
else
echo "download log Not Found!"


serviceBody="
[Unit]
Description=From youtube to telegram upload daemon

[Service]
WorkingDirectory=$(pwd)
ExecStart=$pythonPath -m src.updateManager > $logPath
Restart=always

[Install]
WantedBy=multi-user.target 
"

echo "$serviceBody" > $serviceFilePath/$downloadDirectoryName.service
chmod 644 $serviceFilePath/$downloadDirectoryName.service
systemd daemon-reload


