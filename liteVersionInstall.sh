#!/bin/bash

installPath=/usr/local/
serviceFilePath=/etc/systemd/system

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
if ! git clone https://github.com/RuStyC0der/telegramMusicFromYoutube.git $downloadDirectoryName
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
fi

echo "moving download log..."
if test -f $scriptPath/$downloadedLogFileName
then
cp $scriptPath/$downloadedLogFileName ./
else
echo "download log Not Found!"
fi

serviceBody="
[Unit]
Description=From youtube to telegram upload daemon

[Service]
WorkingDirectory=$(pwd)
ExecStart=$pythonPath -m src.updateManager
Restart=always

[Install]
WantedBy=multi-user.target 
"

echo "$serviceBody" > $serviceFilePath/$downloadDirectoryName.service
chmod 644 $serviceFilePath/$downloadDirectoryName.service

systemctl daemon-reload

echo "
service  already installed
to one time start in background use command:

systemctl start $downloadDirectoryName.service
to use autorun type: 

systemctl enable $downloadDirectoryName.service
systemctl start $downloadDirectoryName.service

prepare first start to create session...
after sesion creat you can stop command using ctrl+c 
"

$pythonPath -m src.updateManager 
