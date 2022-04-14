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


def init_door():
    door = servo.Servo(PWM_DOOR)

    return door
