import board
import neopixel
import time
import pixel_nor
import pixel_laugh


pixels = neopixel.NeoPixel(board.D18, 64)

state = 0
tstart = time.time()
while(True):
    if(state == 0):
        if time.time() - tstart > 1:
            state = 1
            tstart = time.time()
        pixel_data = pixel_laugh.returndata()
        for index,data in enumerate(pixel_data):
            pixels[index] = data
    else:
        if time.time() - tstart > 1:
            state = 0
            tstart = time.time()
        pixel_data = pixel_nor.returndata()
        for index,data in enumerate(pixel_data):
            pixels[index] = data