from machine import Pin
import machine

class TLC5947:
    def __init__(self, clock: Pin = Pin("GP2", Pin.OUT), data: Pin = Pin("GP3", Pin.OUT), latch: Pin = Pin("GP5", Pin.OUT)):
        self.numdrivers = 1
        self._data  = data
        self._clock = clock
        self._latch = latch

        self._latch.low()

        self._spi = machine.SPI(0, sck=self._clock, mosi=self._data, miso=None)

        # self.OE = OE

        self.pwmbuffer = bytearray(36 * 8 * self.numdrivers)         # memset(pwmbuffer, 0, 2 * 24 * n);

        # self.pwmbuffer[20] = 50
        self.write()
        # self.spi = machine.SPI(0)

    def write(self) -> None:
        """Write out the current channel PWM values to the chip.  This is only
        necessary to call if you disabled auto_write in the initializer,
        otherwise write is automatically called on any channel update.
        """
        # First ensure latch is low.
        self._latch.value(False)
        # Write out the bits.
        
        self._spi.write(bytearray(sorted(self.pwmbuffer)))
        
        # Then toggle latch high and low to set the value.
        self._latch.value(True)
        self._latch.value(False)

    def setLed(self, lednum, r,g,b):
        self.setPWM(lednum * 3, r)
        self.setPWM(lednum * 3 + 1, g)
        self.setPWM(lednum * 3 + 2, b)

    def setPWM(self, chan: int, pwm: int):
        if (pwm > 4095):
            pwm = 4095
        try:
            self.pwmbuffer[chan] = pwm
        except:
            pass

