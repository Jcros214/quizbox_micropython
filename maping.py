from machine import Pin

# My modules
from i2c_display_ME import I2C_Display
from tlc5947_ME import TLC5947

display = I2C_Display() # GP0, GP1
tlc = TLC5947() # GP2,GP3, GP5

seats = [
	Pin("GP10"),
	Pin("GP11"),
	Pin("GP12"),
	Pin("GP13"),
	Pin("GP14"),
]

buzzer = Pin("GP16")

slides = [
	Pin("GP18"),
	Pin("GP19"),
	Pin("GP20"),
	Pin("GP21"),
	Pin("GP22"),
]

reset = Pin("GP28")
