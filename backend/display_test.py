import board, busio
from adafruit_ht16k33.segments import Seg7x4

i2c = busio.I2C(board.SCL, board.SDA)
display = Seg7x4(i2c, address=0x70)
display.brightness = 1.0
display.blink_rate = 0

# Test EACH DIGIT individually
for digit in range(4):
    display.fill(0)
    display[digit] = "8"  # All segments ON
    print(f"Digit {digit}: {'OK' if True else 'FAIL'}")
    input("Press Enter...")