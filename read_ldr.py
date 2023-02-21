import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for the LDR
ldr_pin = 17
GPIO.setup(ldr_pin, GPIO.IN)

# Read the LDR value 10 times and print the results
for i in range(10):
    ldr_value = GPIO.input(ldr_pin)
    print("LDR value:", ldr_value)
    time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()
