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

""""
NO MODIFICAR NINGUNO DE LOS VALORES DE VELOCIDAD
"""


# Create your objects here.
motorEV3_3 = Motor(Port.B) #elevación garra
motorEV3_4 = Motor(Port.C) #presión garra

# Función para subir la garra
""""
NO MODIFICAR NINGUNO DE LOS VALORES DE VELOCIDAD
"""
def subir_garra():
    velocidad = 750
    tiempo = 2500
    motorEV3_3.run(-velocidad)
    wait(tiempo)
    motorEV3_3.hold()

# Función para bajar la garra
""""
NO MODIFICAR NINGUNO DE LOS VALORES DE VELOCIDAD
"""
def bajar_garra():
    velocidad = 100
    tiempo = 1000
    motorEV3_3.run(velocidad)
    wait(tiempo)
    motorEV3_3.hold()

# Función para apretar la garra
def apretar_garra():
    velocidad = 500
    tiempo = 2000
    motorEV3_4.run(-velocidad)
    wait(tiempo)
    motorEV3_4.hold()

# Función para abrir la garra
""""
NO MODIFICAR NINGUNO DE LOS VALORES DE VELOCIDAD
"""
def abrir_garra():
    velocidad = 500
    tiempo = 1551
    motorEV3_4.run(velocidad)
    wait(tiempo)
    motorEV3_4.hold()

# Función para reiniciar la garra a una posición específica
def reiniciar_garra():
    motorEV3_3.reset_angle(0)  # Mover motorEV3_3 a la posición inicial
    motorEV3_4.reset_angle(0)  # Mover motorEV3_4 a la posición inicial
    wait(1000)
    motorEV3_3.hold()
    motorEV3_4.hold()


# bajar_garra(500,1000)
# apretar_garra(700,1000)
# subir_garra(400,1000)
# wait(2000)
# bajar_garra(100,1000)
# #abrir_garra(1000,1000)
# subir_garra(100,1000)
# reiniciar_garra()

# abrir_garra()
bajar_garra()
apretar_garra()
subir_garra()
