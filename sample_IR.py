import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2 # import the class with function definitions

DR = 19          # Infrared sensor Right
DL = 16          # Infrared sensor Left

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP) # set Infrared sensor as input, type PUD_UP (pull up resistor)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

try: # catch runtime error in the block of code inside try

        while True: # run forever
        
                DR_status = GPIO.input(DR)
                DL_status = GPIO.input(DL)

                if DR_status == 0 or DL_status == 0:
                        if DR_status == 0 and DL_status != 0: #if the right sensor reads 0, move left
                                print("Object on right")
                                time.sleep(0.1)                                
                        elif DL_status == 0 and DR_status != 0: #if the left sensor reads 0, move right
                                print("Object on left")
                                time.sleep(0.1)
                        elif DL_status == 0 and DR_status == 0:
                                print("Object in the center")
                                time.sleep(0.1)

except KeyboardInterrupt:
        print("Exiting.....")
        GPIO.cleanup();