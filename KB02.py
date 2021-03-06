#-------------------------------------------------------------------
# based on CamJam EduKit 3 - Robotics 
# Worksheet 7 – Varying the speed of each motor with PWM
# This includes a section to take a keyboard input 
#   and drive the motors in teh aproperate direction. 
# 8=forward
# 4=left
# 6=right
# 2=reverse
# any other key = all stop
#------------------------------------------------------------------

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# Settng the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Left():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Your code to control the robot goes below this line
# Modifications to origonal below. 
try:
    while True:
        #print('enter a number')
        KB = input('Choose a number: ')
        print('you entered: '+KB)
        if KB == "8":
            print('pass (answer =8)')
            Forwards()
            time.sleep(0.1)
        elif KB == "4":
            print('LEFT KB = 4')
            Left()
            time.sleep(0.1)
        elif KB == "6":
            print('RIGHT KB = 6')
            Right()
            time.sleep(0.1)
        elif KB == "2":
            print('Back KB = 2')
            Backwards()
            time.sleep(0.1)
        else:
            print('all stop')
            StopMotors()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    StopMotors()
    #GPIO.cleanup()
    print ('Good bye!')



#Forwards()
#time.sleep(1) # Pause for 1 second
#
#Left()
#time.sleep(0.5) # Pause for half a second
#
#Forwards()
#time.sleep(1)
#
#Right()
#time.sleep(0.5)
#
#Backwards()
#time.sleep(0.5)
#

#StopMotors()

#GPIO.cleanup()
