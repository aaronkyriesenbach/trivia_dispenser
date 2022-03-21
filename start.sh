#!/bin/bash

cd /home/pi/trivia_dispenser
git pull
source venv/bin/activate
pip install -r requirements.txt
python main.py
