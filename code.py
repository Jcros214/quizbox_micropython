# My modules
from i2c_display_ME import I2C_Display
from tlc5947_ME import TLC5947

# External modules
from time import sleep

# display = I2C_Display()
tlc = TLC5947()

while True:
    # display.startup()
    for channel in range(24):
        print(channel)
        tlc.setPWM(channel, 50000)
        tlc.write()
        sleep(.5)
        # tlc.setPWM(channel, 0)
        tlc.write()
