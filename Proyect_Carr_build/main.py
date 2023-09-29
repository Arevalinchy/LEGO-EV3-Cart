#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motorEV3 = Motor(Port.A)

# Write your program here.
wait(1000)
a = ev3.buttons.pressed()
while len(a) == 0:
    motorEV3.run(1000)  
    a = ev3.buttons.pressed()
motorEV3.hold()

if len(a) != 0:
    ev3.screen.draw_box(10,10,40,40)
    ev3.screen.print("hola mundo")
    ev3.screen.clear()
    a.clear()
wait(1000)
print("finito")