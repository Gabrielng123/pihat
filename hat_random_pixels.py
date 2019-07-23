#!/usr/bin/env python
from sense_hat import SenseHat

sense = SenseHat()

import random
import time

r = random.randint(0, 7)
print ("the random number is"), r


sense.set_pixel (r, r, (255, 255, 255))

time.sleep (1)
sense.clear()
