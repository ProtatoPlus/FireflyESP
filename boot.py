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
    targets = []
    targetpos = 0
    for x in range(randint(2, 6)):
        targets.append(randint(0, length))
    for x in range(length):
        blinkled(targetpos[0])
        targetpos = targetpos + 1
    targets = 0
    targetpos = 0

while 1 == 1:
    flashlight()
