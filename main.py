import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_matrixkeypad
import board
import digitalio

PIN_RS = digitalio.DigitalInOut(board.D2)
PIN_EN = digitalio.DigitalInOut(board.D3)
PIN_D4 = digitalio.DigitalInOut(board.D4)
PIN_D5 = digitalio.DigitalInOut(board.D17)
PIN_D6 = digitalio.DigitalInOut(board.D27)
PIN_D7 = digitalio.DigitalInOut(board.D22)

if __name__ == '__main__':
    # LCD initialization
    lcd = characterlcd.Character_LCD_Mono(PIN_RS, PIN_EN, PIN_D4, PIN_D5, PIN_D6, PIN_D7, 20, 4)

    lcd.message = "Hello world!"

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
            lcd.message = ''.join(str(k) for k in keys)

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
