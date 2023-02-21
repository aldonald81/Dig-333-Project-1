import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for the LED
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# Blink the LED 5 times
for i in range(5):
    # Turn the LED on
    GPIO.output(led_pin, GPIO.HIGH)
    # Wait for 1 second
    time.sleep(1)
    # Turn the LED off
    GPIO.output(led_pin, GPIO.LOW)
    # Wait for 1 second
    time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()
