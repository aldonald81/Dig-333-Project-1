"""
1. Read value from LDR constantly
2. Fetch weather data on certain LDR value
3. Translate text to speech and play alarm and weather on speaker
"""

import pygame

import RPi.GPIO as GPIO
import time
import requests

from gtts import gTTS
from playsound import playsound

### READ VALUE FROM LDR
mpin=17
tpin=27
GPIO.setmode(GPIO.BCM)
cap=0.000001
adj=2.130620985
i=0
t=0
while t < 1000000:
    print(t)
    GPIO.setup(mpin, GPIO.OUT)
    GPIO.setup(tpin, GPIO.OUT)
    GPIO.output(mpin, False)
    GPIO.output(tpin, False)
    time.sleep(0.2)
    GPIO.setup(mpin, GPIO.IN)
    time.sleep(0.2)
    GPIO.output(tpin, True)
    starttime=time.time()
    endtime=time.time()
    while (GPIO.input(mpin) == GPIO.LOW):
        endtime=time.time()
    measureresistance=endtime-starttime
    
    res=(measureresistance/cap)*adj
    i=i+1
    t=t+res
    if i==10:
        t=t/i
        print(t)
        i=0
        t=0
    
    # if resistance (t) is above some value, exit and trigger the alarm

### FETCH WEATHER DATA FOR CURRENT MOMENT
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

weather_text = f'The temperature in {city} is {temperature} degrees Fahrenheit and the weather is {description}'


### TEXT TO SPEECH AND ANNOUNCE ON ALARM

print("alarm")

## Set off buzzer to wake person up
buzzer_pin = 10
GPIO.setup(buzzer_pin, GPIO.OUT)

print("ALARM GOING OFF \n")
for j in range(5):
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)

text = weather_text

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine to generate speech
tts = gTTS(text=text, lang=language)

# Saving the converted audio in a mp3 file named sample.mp3
tts.save("sample.mp3")


filename = "sample.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


# Playing the converted audio file
#playsound("sample.mp3")


"""
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

"""