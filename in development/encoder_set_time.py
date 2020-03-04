# encoder_set_time 2020-02-20 v00.py
# clock_builder.x_clock_set module

import time
import board
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
import rotaryio as enc
from adafruit_ht16k33.segments import Seg14x4

### DEFINE AND INITIALIZE PINS AND DEVICES ###
# digital inputs and outputs for encoder

i2c = board.I2C()
display = Seg14x4(i2c, address=0x70)
display.brightness = 3
display.fill(0)  # Clear the display
display.print("----")
display.show()


sel_sw = DigitalInOut(board.D9)
sel_sw.direction = Direction.INPUT
sel_sw.pull = Pull.UP

enc = rotaryio.IncrementalEncoder(board.D5, board.D6)

### LISTS AND DICTIONARIES ###

### HELPERS ###

### MAIN CODE SECTION ###

### Main Loop ###

display.print("1234567890")

last_position = None
while True:
    position = enc.position
    if last_position == None or position != last_position:
        print(position, not sel_sw.value)
    last_position = position
    time.sleep(.1)
