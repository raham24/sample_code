import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2 # import the class with function definitions

Ab = AlphaBot2() # Ab = alphabot robot

DR = 19          # Infrared sensor Right
DL = 16          # Infrared sensor Left

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP) # set Infrared sensor as input, type PUD_UP (pull up resistor)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

Ab.setPWMA(20) # set duty cycle for the left motor
Ab.setPWMB(20) # set duty cycle for the right motor

# Duty cycle is used to set the speed of the robot
# Recomended duty cycle is anywhere between 20-30