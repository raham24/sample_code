import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2 # import the class with function definitions

Ab = AlphaBot2()

Ab.setPWMA(20)
Ab.setPWMB(20)

# set duty cycle for the left motor 
# Duty cycle is used to set the speed of the robot
# Recomended duty cycle is anywhere between 20-30

Ab.forward()
time.sleep(0.5)

Ab.stop()
time.sleep(0.1)

Ab.backward()
time.sleep(0.5)

Ab.stop()
time.sleep(0.1)

Ab.right()
time.sleep(0.5)

Ab.stop()
time.sleep(0.1)

Ab.left()
time.sleep(0.5)

Ab.stop()
GPIO.cleanup()