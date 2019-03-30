import board
import neopixel
import pixel_laugh
pixels = neopixel.NeoPixel(board.D18, 64)
pixel_data = pixel_laugh.returndata()
for index,data in enumerate(pixel_data):
    pixels[index] = data