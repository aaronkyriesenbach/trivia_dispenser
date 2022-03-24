import csv
import os
import time

import adafruit_character_lcd.character_lcd_i2c as character_lcd
import board

from Question import *

if __name__ == '__main__':
    print("Script started")

    # LCD initialization
    i2c = board.I2C()
    lcd = character_lcd.Character_LCD_I2C(i2c, 20, 4, address=0x27)
    print("Here")
    lcd.backlight = True
    # lcd.message = "Hello world!"
    # print("Message written")
    #
    while True:
        print("Message written")
        time.sleep(1)

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
