import board
import neopixel
import time
import pixel_nor
import pixel_laugh


pixels = neopixel.NeoPixel(board.D18, 64)
pixel_ini  = [  (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),
                (  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0),(  0,  0,  0)]
state = 0
tstart = time.time()

def light(kao):
    pixel_data = pixel_ini
    if kao == 0 :
        pixel_data = pixel_laugh.returndata()
    elif kao == 1 :
        pixel_data = pixel_nor.returndata()
    else :
        pixel_data = pixel_ini
    for index,data in enumerate(pixel_data):
        pixels[index] = data
'''            
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
'''            