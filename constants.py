import board
import digitalio
import pwmio

BASE_USB_PATH = "/media/usb0"

# LCD
PIN_RS = digitalio.DigitalInOut(board.D2)
PIN_EN = digitalio.DigitalInOut(board.D3)
PIN_D4 = digitalio.DigitalInOut(board.D4)
PIN_D5 = digitalio.DigitalInOut(board.D17)
PIN_D6 = digitalio.DigitalInOut(board.D27)
PIN_D7 = digitalio.DigitalInOut(board.D22)

COLS = 20
ROWS = 4

# Keypad
cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]
rows = [digitalio.DigitalInOut(x) for x in (board.D26, board.D16, board.D20, board.D21)]
keys = [(1, 2, 3, "A"),
        (4, 5, 6, "B"),
        (7, 8, 9, "C"),
        (0, "F", "E", "D")]

# Servos
PWM_WHEEL = pwmio.PWMOut(board.D12, frequency=50)
PWM_DOOR_1 = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)
PWM_DOOR_2 = pwmio.PWMOut(board.D8, duty_cycle=2 ** 15, frequency=50)
