# Notes: 
# Remember to invert logic when using pullup resistors







import machine
from time import time

# Declarations
from maping import display, tlc, seats, buzzer, slides, reset

r = 1000
g = 1000
b = 1000


# Globals
boxState = 0

timer_start = 0
timer = 32

refreshTLC = False


while True:
    if boxState == 1:
        for index,seat,switch in zip([0,1,2,3,4,5],seats,slides): # Box is unlocked
            if switch.value() and  seat.value(): # If enabled and standing
                tlc.setLed(index, r,g,b)
            else:
                tlc.setLed(index, 0,0,0)
        tlc.write()

    elif boxState == 2: # Box is armed
        for index,seat,switch in zip([0,1,2,3,4,5],seats,slides): # Box is armed
            if switch.value() and  seat.value(): # If enabled and standing
                timer_start = time()
                tlc.setLed(index, r,g,b)
                tlc.setLed(5, 2000, 0, 0)
                tlc.setLed(6, 2000, 0, 0)
                tlc.write()

                # buzz
                # display write
                boxState = 3

    elif boxState == 3:
        if timer > 0:
            if round(time() - timer_start) != timer:
                timer = round(time() - timer_start)
                # display
                if timer == 20:
                    ...
                    # Buzz
                elif timer == 0:
                    ...
                    # buzz
                    
        else:
            # display
            timer_start = 0
            boxState = 1