# Chaser w/ Tails
# @todbot 27 may 2021
import time, random
import board, neopixel
num_pixels = 24  # Number of NeoPixels
pixel_pin = board.D0  # Pin where NeoPixels are connected
ORDER = neopixel.GRB
leds = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

my_color = (55,200,220)
dim_by = 20 # dim amount, higher = shorter tails
pos = 0
while True:
    leds[pos] = my_color
    leds[0:] = [[max(i-dim_by,0) for i in l] for l in leds] # dim all by (dim_by,dim_by,dim_by)
    pos = (pos+1) % num_pixels # move to next position
    leds.show() # only write to LEDS after updating them all
    time.sleep(0.05)
