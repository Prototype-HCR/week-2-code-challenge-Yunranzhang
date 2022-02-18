import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.2
# create a color as a tuple value
purple = 0xaf7fd4
green = 0x70ccaa
red = 0xfc1717

pixels.fill(0)


button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)

button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)


# delare a boolean variable
led_state = True

while True:
    # gather all the input values from sensors
    # print the values of our button_a project
    button_a_read = button_a.value
    button_b_read = button_b.value



    # print("button a read is:", button_a_read)
    # if the value of the led_state is True
    if button_a_read and button_b_read:
        pixels.fill(purple)
    elif button_a_read:
        pixels.fill(green)
    elif button_b_read:
        pixels.fill(red)
    else:
        pixels.fill(0)
        led_state = False
    # turn the neopixel off
    # time.sleep(0.1)
