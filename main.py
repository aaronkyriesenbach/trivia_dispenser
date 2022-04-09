from hwinit import *

# Hardware initialization
lcd = init_lcd()
keypad = init_keypad()


def get_pressed_key(pressed_keys):
    return ''.join(str(k) for k in pressed_keys)


if __name__ == '__main__':
    lcd.message = "Hello world!"

    while True:
        keys = keypad.pressed_keys
        if keys:
            lcd.clear()
            lcd.message = get_pressed_key(keys)

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
