"""
1. Read value from LDR constantly
2. Fetch weather data on certain LDR value
3. Translate text to speech and play alarm and weather on speaker
"""
import sys

import pygame

import RPi.GPIO as GPIO
import time
import requests

from gtts import gTTS
from playsound import playsound

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT) #led
GPIO.output(6, GPIO.LOW)

GPIO.setup(5, GPIO.OUT) #led
GPIO.output(5, GPIO.LOW)

def button_callback(channel):
    print("Button was pushed!")
    GPIO.cleanup() # Clean up
    sys.exit()
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge


pin=4

wakeup = False
count=0
#check time is in the morning: between 6am and 8pm
while count < 50000: #WOULD TECHNIcALLY BE > THAN SINCE IT WOULD BE GETTING LIGHTER

    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    time.sleep(.1)
    GPIO.setup(pin, GPIO.IN)

    while(GPIO.input(pin) == GPIO.LOW):
        count += 1
    
    print(count)


## Run until the user pushes the button or it has run 4 times
GPIO.setup(10,GPIO.OUT)# buzzer

times = 0
button_pushed = False
while times < 4 :
    ### FETCH WEATHER DATA FOR CURRENT MOMENT
    api_key = 'f95cf4e0206468f647dd9c15d5092f6e'
    lat = 35.4993
    long = -80.8487
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}'
    # https://api.openweathermap.org/data/2.5/weather?lat=35.4993&lon=80.8487&appid=f95cf4e0206468f647dd9c15d50

    # Send the HTTP request and receive the response
    response = requests.get(url)

    # Parse the JSON response data into a Python dictionary
    data = response.json()

    # Extract the temperature and description from the data
    temperature = round((int(data['main']['temp']) - 273.15) * 1.8 + 32, 0)
    description = data['weather'][0]['description']

    weather_text = f'Get up sunshine! Lets get after it today. Let me give you a run down of the weather. The temperature in Davidson is {temperature} degrees Fahrenheit and the weather is {description}'


    ### TEXT TO SPEECH AND ANNOUNCE ON ALARM

    print("alarm")
    
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


    times += 1

    snooze = 15
    print("snoozing")

    if(times == 1):
        # Light up an LED for each snooze
        GPIO.output(6, GPIO.HIGH)

    if(times == 2):
        # Light up an LED for each snooze
        GPIO.output(5, GPIO.HIGH)

    #>>>>>>>>>light up other leds for each wait

    time.sleep(snooze)


GPIO.cleanup() # Clean up



