#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
motorEV3 = Motor(Port.A)  # Rueda derecha
motorEV3_2 = Motor(Port.D)  # Rueda izquierda

robot = DriveBase(motorEV3_2,motorEV3,56,220)
speed = 200 # velocidad mm/s equivalente 20 cm/s
distancia = 500 # Una distancia inicial de 50 cm
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
    robot.straight(-distancia)
    robot.stop()    

#Simulamos la subida de la rampa y el giro de 90 grados
adelante(speed,distancia)
subirRampa(speed/2,1420)
adelante(speed,distancia/2)
robot.turn(-90)
robot.stop()
adelante(speed,distancia)


# # Set the speed of the motors (adjust as needed)
# motor_speed = -500
# motor_speed2 = -280

# # Define the duration of movement in milliseconds (5 seconds in this example)
# duration = 12200

# # Write your program here.
# motorEV3.run(motor_speed)
# motorEV3_2.run(motor_speed)

# # Wait for the specified duration
# wait(duration)


# # # Stop the motors
# motorEV3.stop()
# motorEV3_2.stop()

# motorEV3_2.run(motor_speed)
# wait(1500)
# motorEV3_2.stop()


# motorEV3.run(motor_speed)
# motorEV3_2.run(motor_speed)

# # Wait for the specified duration
# wait(1000)
# motorEV3.stop()
# motorEV3_2.stop()




