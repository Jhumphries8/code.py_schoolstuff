# Write your code here :-)

# imports libraries used in code
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
    forward()
    time.sleep(1.8)
    right()
    time.sleep(.3)
    forward()
    time.sleep(2)
    right()
    time.sleep(.5)
    stop()
    time.sleep(4)
