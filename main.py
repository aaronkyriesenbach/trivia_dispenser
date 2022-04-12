import csv
import math
import os
import time

from Question import *
from hwinit import *

# Hardware initialization
lcd = init_lcd()
keypad = init_keypad()
wheel = init_dispenser_wheel()
door = init_door()


def display_message(message: str):
    lcd.clear()
    lines = []

    for i in range(0, len(message), 20):
        if i + 20 > len(message):
            lines.append(message[i:])
        else:
            lines.append(message[i:i + 20])

    lines = [line.strip() for line in lines]

    for i in range(len(lines)):
        lcd.cursor_position(0, i)
        lcd.message = lines[i]


def get_pressed_key(pressed_keys):
    return ''.join(str(k) for k in pressed_keys)


def dispense():
    # Move forwards for 0.5 secs
    wheel.throttle = 1
    time.sleep(0.5)

    # Pause for 0.1 secs
    wheel.throttle = 0
    time.sleep(0.5)

    # Run backwards for 0.5 secs
    wheel.throttle = -1
    time.sleep(0.5)
    wheel.throttle = 0


def get_questions():
    questions: set[Question] = set()

    with open((BASE_USB_PATH + "/questions.csv") if os.path.isdir(BASE_USB_PATH) else "test_questions.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            text = row[0]
            answers: set[Answer] = set()

            if len(row) == 2:
                answers.add(Answer(float(row[1]), True))
            else:
                for i in range(1, len(row), 2):
                    answers.add(Answer(row[i], bool(int(row[i + 1]))))

            questions.add(Question(text, frozenset(answers),
                                   QuestionType.NUMERICAL if len(row) == 2 else QuestionType.MULTIPLE_CHOICE))

    return questions


def get_num_answer_from_str(answer: str):
    try:
        num_answer = int(answer)
    except ValueError:
        num_answer = ord(answer) - 64

    if 1 <= num_answer <= 4:
        return num_answer
    else:
        return None


def display_answer_options(answers):
    for answer in answers:
        display_message(answer.text)
        time.sleep(3)

    display_message("What is the correct answer?")


if __name__ == '__main__':
    # Question initialization
    questions = get_questions()
    if len(questions) < 4:
        display_message("Please provide at least 4 questions!")
        exit(1)
    CORRECT_ANSWER_THRESHOLD = math.floor(len(questions) * 0.75)

    # Play game
    while True:
        display_message("Welcome to the trivia dispenser!")
        time.sleep(5)

        correct_answer_count = 0
        for question in questions:
            display_message(question.text)
            time.sleep(3)

            if question.question_type == QuestionType.MULTIPLE_CHOICE:
                answers = list(question.answers)
                display_answer_options(answers)

                while True:
                    keys = keypad.pressed_keys

                    if keys:
                        answer = get_pressed_key(keys)

                        if answer == 'F':
                            display_answer_options(answers)
                        else:
                            num_answer = get_num_answer_from_str(answer)

                            if num_answer:
                                if answers[num_answer - 1].correct:
                                    display_message("Correct!")
                                    correct_answer_count += 1
                                else:
                                    display_message("Incorrect :(")
                                time.sleep(1)
                                break
                            else:
                                display_message("Please enter a valid answer!")
            else:
                answerstr = ""
                while True:
                    display_message(answerstr)

                    keys = keypad.pressed_keys

                    if keys:
                        pressed_key = get_pressed_key(keys)

                        if pressed_key.isdigit():
                            answerstr += pressed_key;
                        elif pressed_key == 'D':
                            answerstr = answerstr[:-1]


            if correct_answer_count >= CORRECT_ANSWER_THRESHOLD:
                break

        if correct_answer_count >= CORRECT_ANSWER_THRESHOLD:
            display_message("You win!")
            dispense()
        else:
            display_message("You lose - better luck next time!")
        time.sleep(5)
