import csv
import os
import time
import digitalio
import board
import adafruit_matrixkeypad

import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

from Question import *

if __name__ == '__main__':
    print("Script started")

    # LCD initialization
    lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=GPIO.BOARD, cols=20, rows=4)
    lcd.clear()
    lcd.write_string("Hello world, this is yet another message!!")

    # Keypad initialization
    cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
    rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D16, board.D20, board.D21)]
    keys = [(1, 2, 3, "A"),
            (4, 5, 6, "B"),
            (7, 8, 9, "C"),
            (0, "F", "E", "D")]
    keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    while True:
        keys = keypad.pressed_keys
        if keys:
            lcd.clear()
            lcd.write_string(keys)

    # Question initialization
    questions: set[Question] = set()

    BASE_USB_PATH = "/media/usb0"
    with open((BASE_USB_PATH + "/questions.csv") if os.path.isdir(BASE_USB_PATH) else "test_questions.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            qstring = row[0]
            answers: set[Answer] = set()
            for i in range(1, len(row), 2):
                answer = Answer(row[i], bool(row[i + 1]))
                answers.add(answer)

            questions.add(Question(qstring, frozenset(answers)))

    for q in questions:
        print(q)
