import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4

# Currently doesn't work
class Clock:
    def __init__(self, controller):
        self.controller = controller
        self.colon_on = True

        # I2C + display setup
        i2c = busio.I2C(board.SCL, board.SDA)
        display = Seg7x4(i2c, address=0x70)

        display.brightness = 1.0
        display.blink_rate = 0

    def update(self):
        if self.controller.running:
            now = time.localtime()   # get current time
            hour = now.tm_hour
            minute = now.tm_min

            # Optional: convert to 12-hour format
            if hour == 0:
                hour = 12
            elif hour > 12:
                hour -= 12

            # Format time as HHMM
            time_str = f"{hour:02d}{minute:02d}"

            # Display digits
            self.display[0] = time_str[0]
            self.display[1] = time_str[1]
            self.display[2] = time_str[2]
            self.display[3] = time_str[3]

            # Blink colon
            self.display.colon = self.colon_on
            self.colon_on = not self.colon_on