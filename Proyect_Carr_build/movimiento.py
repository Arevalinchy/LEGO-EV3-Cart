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
def subirRampa(speed,distancia):
    robot.settings(speed)
    robot.straight(-distancia/2)
    robot.stop()
    robot.settings(speed/2)
    robot.straight(-distancia/2)
    robot.stop()
  
def girar_derecha():
    robot.turn(-90)
    robot.stop()
  

def girar_izquierda():
    robot.turn(90)
    robot.stop()
def giro_Completo():
    robot.turn(180)
    robot.stop()


adelante(speed,distancia)


# ------------------------------------------------------------------------------------------------------------------
# Lo trabajado el 30 oct
# ------------------------------------------------------------------------------------------------------------------
# Función para realizar un giro en función de un ángulo en grados
def girar(angulo, velocidad, distancia_entre_ruedas):
    # Convertir el ángulo de grados a radianes
    angulo_radianes = math.radians(angulo)

    # Calcular el radio de giro (la mitad de la distancia entre ruedas)
    radio_giro = distancia_entre_ruedas / 2

    # Calcular la distancia recorrida por cada rueda
    distancia_rueda = radio_giro * angulo_radianes # distancia en centímetros

    # Configurar la velocidad de las ruedas
    motorEV3.run(velocidad)
    motorEV3_2.run(velocidad)

    # Realizar el giro bloqueando una rueda y dejando que la otra se mueva
    if angulo > 0:
        motorEV3_2.run_target(velocidad, distancia_rueda)
    else:
        motorEV3.run_target(velocidad, distancia_rueda)

    # Esperar a que el giro se complete
    wait(1000)

    # Detener ambas ruedas
    motorEV3.stop()
    motorEV3_2.stop()

# # ---
# # Función para realizar un giro en un semicírculo
# def girar_semici­rculo(velocidad, radio, distancia_entre_ruedas):
#     # Calcular la distancia que debe recorrer cada rueda
#     distancia_rueda = math.pi * radio  # Semicírculo, por lo que usamos pi

#     # Configurar la velocidad de las ruedas
#     motorEV3.run(velocidad)
#     motorEV3_2.run(velocidad)

#     # Realizar el giro bloqueando una rueda y dejando que la otra se mueva
#     if radio > 0:
#         motorEV3_2.run_target(velocidad, distancia_rueda)
#     else:
#         motorEV3.run_target(velocidad, distancia_rueda)

#     # Esperar a que el giro se complete
#     wait(1000)

#     # Detener ambas ruedas
#     motorEV3.stop()
#     motorEV3_2.stop()

# '''
# Movimiento de la garra
# '''

# Función para subir la garra
def subir_garra(velocidad, tiempo):
    motorEV3_3.run(velocidad)
    wait(tiempo)
    motorEV3_3.hold()

# Función para bajar la garra
def bajar_garra(velocidad, tiempo):
    motorEV3_3.run(-velocidad)
    wait(tiempo)
    motorEV3_3.hold()

# Función para apretar la garra
def apretar_garra(velocidad, tiempo):
    motorEV3_4.run(velocidad)
    wait(tiempo)
    motorEV3_4.hold()

# Función para abrir la garra
def abrir_garra(velocidad, tiempo):
    motorEV3_4.run(-velocidad)
    wait(tiempo)
    motorEV3_4.hold()

# Función para reiniciar la garra a una posición específica
def reiniciar_garra():
    motorEV3_3.run_target(200, 0)  # Mover motorEV3_3 a la posición inicial
    motorEV3_4.run_target(1000, 0)  # Mover motorEV3_4 a la posición inicial
    motorEV3_3.hold()
    motorEV3_4.hold()



