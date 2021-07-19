#
# Kaleidoscope_Eyes_NeoPixel_LED_Goggles.py
# from https://learn.adafruit.com/kaleidoscope-eyes-neopixel-led-goggles-trinket-gemma/circuitpython-code


import time
import board
import neopixel
#
try:
    import urandom as random  # for v1.0 API support
except ImportError:
    import random

num_pixels = 24  # Number of NeoPixels
pixel_pin = board.D0  # Pin where NeoPixels are connected

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        # time.sleep(wait)

# Color test, should show Red, Green, then Blue on startswith
pixels.fill((255, 0, 0))
pixels.show()
time.sleep(1)
pixels.fill((0, 255, 0))
pixels.show()
time.sleep(1)
pixels.fill((0, 0, 255))
pixels.show()
time.sleep(1)

while True:

    rainbow_cycle(0.000001)  # rainbow cycle with 1ms delay per step