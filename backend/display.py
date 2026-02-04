import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4

i2c = busio.I2C(board.SCL, board.SDA)
display = Seg7x4(i2c)

# Clear display
display.fill(0)
time.sleep(0.5)

# Test each digit with 8
for digit in range(4):
    display.fill(0)
    display[digit] = '8'
    time.sleep(0.5)

# Cycle 0–9 on each digit
for digit in range(4):
    for num in range(10):
        display.fill(0)
        display[digit] = str(num)
        time.sleep(0.3)
