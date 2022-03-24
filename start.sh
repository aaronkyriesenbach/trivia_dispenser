#!/bin/bash

cd /home/pi/trivia_dispenser
git pull
source venv/bin/activate
pip install -r requirements.txt
echo "Starting Python script"
python main.py
#journalctl -e --user-unit trivia-dispenser.service >> /media/usb/test
