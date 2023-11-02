# Write your code here :-)
# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii
import board
import busio
import digitalio
import time

from dabble import Dabble

dabble = Dabble(board.GP0, board.GP1, debug=True)

import time
import board
import digitalio
import pwmio


# Import section of adafruit motor library
from adafruit_motor import motor


# Initializes the variables controlling the wheels and assigns them a gp input
left_forward = board.GP12
left_backward = board.GP13

# Tells the pico these are outputs
pwm_La = pwmio.PWMOut(left_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_backward, frequency=10000)

# configuration line
Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
# Initializes the variable Left_Motor_speed
Left_Motor_speed = 0

right_forward = board.GP17
right_backward = board.GP16


pwm_La = pwmio.PWMOut(right_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(right_backward, frequency=10000)

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Right_Motor_speed = 0

def forward():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

def backwards():
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed

def left():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

def right():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

def stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed

while True:
    message = dabble.read_message() # command to take input from bluetooth module
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            forward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            backwards()
            print("Move both motors backward")
        elif (message.right_arrow_pressed):
            right()
            print("Move left motor forward and right motor backward")
        elif (message.left_arrow_pressed):
            left()
            print("Move left motor backward and right motor forward")
        elif (message.no_direction_pressed):
            stop()
            print("Stop both motors")
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
