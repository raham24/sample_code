from adafruit_servokit import ServoKit
import time
import RPi.GPIO as GPIO

# if you get the library missing error, run the following command in your terminal
# sudo pip3 install adafruit-circuitpython-servokit

# Minimum and Maximum impulse
min_imp = 500
max_imp = 2500

# Minimum and Maximum angle
min_angle = 0
max_angle = [180,120] # different max angle for different servos
             
num_serv = 2 # number of servos controlled by the controller

pca = ServoKit(channels = 16) # declare our controller and the channels (we have 16 channel)

def initialize_servos(): 
    # this function is used to ser max and min vals for impulse and each servo
    for i in range(num_serv):
        pca.servo[i].set_pulse_width_range(min_imp, max_imp)

def test():
    # testing function for the servo

    for i in range(num_serv): # external for loop, goes through all the servos
        for j in range(min_angle, max_angle[i], 1): # internal for loop #1, moves the servo from min to max angle
            print(f"Set angle {j} for servo {i}")
            pca.servo[i].angle = j
            time.sleep(0.5)
        for j in range(max_angle[i], min_angle, -1): # internal for loop #2, moves the servo from max to min angle
            print(f"Set angle {j} for servo {i}")
            pca.servo[i].angle = j
            time.sleep(0.5)
        pca.servo[i].angle = None # VERY IMPORTANT. Make sure to use this to avoid any excess power usage
        time.sleep(1)
    
if __name__ == '__main__':
    initialize_servos()
    test()
    print("Test Complete")
    GPIO.cleanup()