import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

CTR = 7 # joystick pushed in
A = 8   # joystick up
B = 9   # joystick right
C = 10  # joystick left
D = 11  # joystick down
BUZ = 4 # Buzzer pin
	
GPIO.setmode(GPIO.BCM)  # set mode to BCM
GPIO.setwarnings(False) # ignore warnings

# Setup all the joystick actions as inputs
GPIO.setup(CTR,GPIO.IN,GPIO.PUD_UP) 
GPIO.setup(A,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(B,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(C,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(D,GPIO.IN,GPIO.PUD_UP)

# set buzzer as output
GPIO.setup(BUZ,GPIO.OUT)

def beep_once():  # func to beep once
	GPIO.output(BUZ,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(BUZ,GPIO.LOW)


try:
	while True:
		if GPIO.input(CTR) == 0: # if joystick pressed in the middle            
			beep_once();
			print("center")
			while GPIO.input(CTR) == 0:
				time.sleep(0.01)
		elif GPIO.input(A) == 0: # if joystick pressed to the up position
			beep_once();
			print("up")
			while GPIO.input(A) == 0:
				time.sleep(0.01)
		elif GPIO.input(B) == 0: # if joystick pressed to the right
			beep_once();
			print("right")
			while GPIO.input(B) == 0:
				time.sleep(0.01)
		elif GPIO.input(C) == 0: # if joystick pressed to the left
			beep_once();
			print("left")
			while GPIO.input(C) == 0:
				time.sleep(0.01)
		elif GPIO.input(D) == 0: # if joystick pressed to the down postition
			beep_once();
			print("down")
			while GPIO.input(D) == 0:
				time.sleep(0.01)
			
except KeyboardInterrupt:
	GPIO.cleanup()
