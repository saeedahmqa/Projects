
import RPi.GPIO as GPIO
import time

# declare the sensor and buz pin
sensor_pin = 23
buz_pin = 26

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(buz_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(sensor_pin):
            # If no object is near
            GPIO.output(buz_pin, False)
            while GPIO.input(sensor_pin):
                time.sleep(0.2)
        else:
            # If an object is detected
            GPIO.output(buz_pin, True)
except KeyboardInterrupt:
    GPIO.cleanup()
