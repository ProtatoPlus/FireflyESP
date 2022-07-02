import machine, neopixel
import time
import urandom
bright = 0
length = 8
np = neopixel.NeoPixel(machine.Pin(4), length + 1)

def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val

def blinkled(led):
    global bright
    time = range(255)
    bright = 255
    for x in time:
        np[led] = (bright, bright, 0)
        np.write()
        bright = bright - 1
    np[led] = (0, 0, 0)
    np.write()
    

def flashlight():
    for x in range(length):
        blinkled(randint(0, length))

while 1 == 1:
    flashlight()
