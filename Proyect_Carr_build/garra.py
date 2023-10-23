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
motorEV3_3 = Motor(Port.B) #elevación garra
motorEV3_4 = Motor(Port.C) #presión garra



for i in range(2):

    motorEV3_4.run(1000)  
    wait(1000)
    motorEV3_4.hold()

    motorEV3_3.run(200)  
    wait(500)
    motorEV3_3.hold()

    motorEV3_4.run(-1000)  
    wait(1000)
    motorEV3_4.hold()

    motorEV3_3.run(-200)  
    wait(500)
    motorEV3_3.hold()
