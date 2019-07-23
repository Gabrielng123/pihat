#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()



yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
speed = 0.05

message = "Goteem!"

sense.show_message(message, speed, text_colour=red, back_colour=blue)

sense.clear()

