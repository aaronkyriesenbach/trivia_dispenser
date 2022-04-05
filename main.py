import csv
import os
import time

from RPi import GPIO
from RPLCD.gpio import CharLCD

from Question import *

if __name__ == '__main__':
    print("Script started")

    # LCD initialization
    lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=GPIO.BOARD, cols=20, rows=4)
    print("Here")
    lcd.write_string("Hello world, this is another message!!")
    time.sleep(5)

    # Question initialization
    questions: set[Question] = set()

    BASE_USB_PATH = "/media/pi/questionusb"
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
