import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_matrixkeypad
from adafruit_motor import servo

from constants import *


def init_lcd():
    return characterlcd.Character_LCD_Mono(PIN_RS, PIN_EN, PIN_D4, PIN_D5, PIN_D6, PIN_D7, COLS, ROWS)


def init_keypad():
    return adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


def init_dispenser_wheel():
    wheel = servo.ContinuousServo(PWM_WHEEL)

    return wheel


def init_doors():
    door1 = servo.Servo(PWM_DOOR_1)
    door2 = servo.Servo(PWM_DOOR_2)

    door1.angle = 180
    door2.angle = 0

    return door1, door2
