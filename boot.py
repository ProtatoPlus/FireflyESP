import machine, neopixel
import time
import urandom
import copy

length = 100
np = neopixel.NeoPixel(machine.Pin(4), length + 1)

#Most firefly flashes are 0.2-0.3 sec long; however, it takes sophisticated equipment
#to measure such short intervals. So in practice I will use comparative descriptions.
#A “normal flash” is 0.2-0.3 sec long. A “snappy flash” is a faster/shorter than normal flash.

blinkyBugStatus = {
    'ticksUntilAction': 0,
    'nextActionType': 0, # 0 = normal, 1 = snappy
    'currentAction': 0,
    'actionTickstate': 20, # "count down" for the current action
    'pulseStreachTicks': 0, # add some variance for the 0.2 - 0.3ish range
    'wavlengthSkew': 0 # Is this a species with red wavlength chemestry
    }
 
BLINKY_BUGS = []

animations = [[10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,10,0],
              [10,10,20,20,25,25,50,50,75,75,120,120,150,150,200,200,255,255,150,100,50,40,30,20,10,0],
              [10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,10,0,10,20,25,50,75,120,120,150,200,255,255,200,150,100,50,40,30,20,10,0]]

def init_bugs():
    for i in range(length):
        BLINKY_BUGS.append(copy.copy(blinkyBugStatus))
        BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['actionTickstate'] + randint(100,1000)
        BLINKY_BUGS[i]['currentAction'] = BLINKY_BUGS[i]['nextActionType']
        BLINKY_BUGS[i]['nextActionType'] = randint(0,len(animations)-1)
        BLINKY_BUGS[i]['wavlengthSkew'] = randint(0,1)
        BLINKY_BUGS[i]['actionTickstate'] = 20


def do_tick():
    for i in range(length):
        if (BLINKY_BUGS[i]['ticksUntilAction'] == 0): # reset ticks until next,
            BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['actionTickstate'] + randint(100,1000)
            BLINKY_BUGS[i]['currentAction'] = BLINKY_BUGS[i]['nextActionType']
            BLINKY_BUGS[i]['nextActionType'] = randint(0,len(animations)-1)
            BLINKY_BUGS[i]['wavlengthSkew'] = randint(0,1)
            BLINKY_BUGS[i]['actionTickstate'] = 0
        else:
            BLINKY_BUGS[i]['ticksUntilAction'] = BLINKY_BUGS[i]['ticksUntilAction'] - 1
            if (BLINKY_BUGS[i]['actionTickstate'] < len(animations[BLINKY_BUGS[i]['currentAction']])):
                intensity = animations[BLINKY_BUGS[i]['currentAction']][BLINKY_BUGS[i]['actionTickstate']]
                BLINKY_BUGS[i]['actionTickstate'] = BLINKY_BUGS[i]['actionTickstate'] + 1
                #if (BLINKY_BUGS[i]['wavlengthSkew'] == 0):
                np[i] = (int(intensity - (intensity * 0.12549)), intensity, 0)
                #else:
                #    np[i] = (intensity, intensity, 0)
    np.write()


def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val
        
init_bugs()

while 1 == 1:
    do_tick()
