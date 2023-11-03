#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

# Create your objects here.
ev3 = EV3Brick()
motorEV3 = Motor(Port.A)  # Rueda derecha
motorEV3_2 = Motor(Port.D)  # Rueda izquierda
motorEV3_3 = Motor(Port.B) #elevación garra
motorEV3_4 = Motor(Port.C) #presión garra
dist_llantas= 2200 #distancia entre llantas
robot = DriveBase(motorEV3_2,motorEV3,56,220)
speed = 200 # velocidad mm/s equivalente 20 cm/s
distancia = 5000 # Una distancia inicial de 50 cm
angulo = 90 #Angulo en grados
robot.settings(speed)

#funcion que lleva el robot hacia adelante, ajusta la velocidad, mueve y luego se detiene.
def adelante(speed,distancia):
    robot.settings(speed)
    robot.straight(-distancia)   
    robot.stop()

#Funcion pensada para subir la rampa, esta contempla el movimiento completo
def subirRampa():
    robot.settings(1000)
    robot.straight(-1900)
    robot.stop()

#355
def giro_derecha():
    robot.turn(-90)
    robot.stop()
  
def giro_izquierda():
    robot.turn(100)
    robot.stop()

def giro_completo():
    robot.turn(180)
    robot.stop()
def giro(grados):
    robot.turn(grados) #- a la izquierda + a la derecha
    robot.stop()

def giro_de_arco_der(speed,r, w=220):
    coef = (2*r - w) / (2*r + w)
    motorEV3.run(-abs(coef*speed)) #derecha
    motorEV3_2.run(-speed) #izquierda
    wait(5000) # 5000ms = 5s
    motorEV3.stop()
    motorEV3_2.stop()

def giro_de_arco_izq(speed,r, w=220):
    coef = (2*r - w) / (2*r + w)
    motorEV3_2.run(-abs(coef*speed)) #derecha
    motorEV3.run(-speed) #izquierda
    wait(5000) # 5000ms = 5s
    motorEV3_2.stop()
    motorEV3.stop()
# '''
# Movimiento de la garra
# '''

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
    tiempo = 1200
    motorEV3_3.run(velocidad)
    wait(tiempo)
    motorEV3_3.hold()

# Función para apretar la garra
def apretar_garra():
    velocidad = 500
    tiempo = 2150
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
    motorEV3_3.run_target(200, 0)  # Mover motorEV3_3 a la posición inicial
    motorEV3_4.run_target(1000, 0)  # Mover motorEV3_4 a la posición inicial
    motorEV3_3.hold()
    motorEV3_4.hold()

def recoger_objeto():
    bajar_garra()
    apretar_garra()
    subir_garra()

def dejar_objeto():
    bajar_garra()
    abrir_garra()
    subir_garra()

"""

Aquí se programará la rutina.
Solo se deben llamar las funciones

"""

# wait(20000)
# adelante(5000,1000)
# recoger_objeto()
# wait(5000)
# adelante(5000,1000)
# giro_izquierda()
# adelante(5000,300)
# dejar_objeto()
# giro(95)
# wait(2000)
# giro_de_arco(450,280) 
# con 200 hace menos de 90 grados pero más de 45
#con 450 se obtiene un ángulo de 112 grados

# wait(10000)
# adelante(1000,1000) # +- un metro (98.5 cms siendo exacto)
# wait(5000)
# adelante(1000,1000)
# wait(5000)
# adelante(1000,1000)
# wait(5000)
# adelante(1000,1000)
# wait(5000)

# adelante(1000,1000)
# wait(5000)
# adelante(200,1000)
# wait(5000)
# subirRampa()

# giro_de_arco(500,210)

# Prueba en pista 1
# adelante(1000,711)
# subirRampa()
# adelante(1000,500)
# giro(-86)
# adelante(1000,813)
# recoger_objeto()
# adelante(1000,813)
# giro_de_arco(300,250)
# adelante(1000,558)
# giro_de_arco(300,250)
# giro(86) # pero en realidad son 58, es por el desfase
# adelante(1000,742)
# giro(-52) # pero en realidad son 48, es por el desfase
# adelante(1000,700)
# giro(54) # pero en realidad son 50, es por el desfase
# adelante(1000,853)

# giro_de_arco_izq(440,500) # 190,200 para dar la curva
giro_de_arco_izq(374,344) # para una curva que mide 58
motorEV3_2.run(-180)
wait(1000)
motorEV3_2.stop()



