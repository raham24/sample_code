import time

from rpi_ws281 import Adafruit_NeoPixel, Color

#if you get library missing error, run this command: sudo pip install rpi_ws281x on your terminal

# LED strip configuration:
LED_COUNT      = 4       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

# initialize the strip with all the details
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

led_off = Color(0, 0, 0)
red = Color(255, 0, 0)
blue = Color(30, 144, 255)
green = Color(50, 205, 50)
yellow = Color(254, 224, 0)
#some led colors. you can change this to anything that you want to.

print ("Turning on LEDs, press Ctrl+C to turn them off")

try:
    strip.begin()
    #start configuring LEDs. Only need to do it once
    
    strip.setPixelColor(0,red)
    strip.setPixelColor(1, green)
    strip.setPixelColor(2, blue)
    strip.setPixelColor(3, yellow)
    #set colors for each LEDs. They are reffered as elements in an array where first is at index 0
    
    strip.show()
    #Turn on the LEDs

except KeyboardInterrupt:
    print("Turning off LEDs")

    # for loop to set all LEDs to turn off
    for i in range(strip.numPixels())
        strip.setPixelColor(i,led_off)
    strip.show()