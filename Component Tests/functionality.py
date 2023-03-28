import RPi.GPIO as GPIO
import time
import requests


# Set the GPIO pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for the components
ldr_pin = 17
GPIO.setup(ldr_pin, GPIO.IN)

buzzer_pin = 18
GPIO.setup(buzzer_pin, GPIO.OUT)

# Run until LDR value == 1
ldr_value = GPIO.input(ldr_pin)
i = 0
while ldr_value != 1:
    ldr_value = GPIO.input(ldr_pin)
    print("LDR value:", ldr_value)
    time.sleep(1)

    # JUST FOR NOW -- until we get analog data
    i+=1
    if i > 10: ldr_value = 1

### Fetch weather data
api_key = 'f95cf4e0206468f647dd9c15d5092f6e'
city = 'Davidson'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
# https://api.openweathermap.org/data/2.5/weather?lat=35.4993&lon=80.8487&appid=f95cf4e0206468f647dd9c15d50

# Send the HTTP request and receive the response
response = requests.get(url)

# Parse the JSON response data into a Python dictionary
data = response.json()

# Extract the temperature and description from the data
temperature = round((int(data['main']['temp']) - 273.15) * 1.8 + 32, 0)
description = data['weather'][0]['description']


### Set off alarm
print("ALARM GOING OFF \n")
for j in range(5):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)

print(f'The temperature in {city} is {temperature} degrees Fahrenheit.')
print(f'The weather is {description}.')


# Clean up the GPIO pins
GPIO.cleanup()

