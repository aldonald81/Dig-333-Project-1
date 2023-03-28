# Sunset Alarm

## Developer's Statement
The Sunrise Alarm is an alarm that goes off when the sun rises based on the amount of light that is in the room and tells you information about the day such as the current weather information. The purpose of this alarm is to wake you up with the sun, so that you can get up and get after the day early. Some of the features of the alarm include a text-to-speech model that fetches and tells you the current weather, LEDs that let you know how many times the alarm has been snoozed, an LDR that records the amount of light in the room, and an on/off button that allows you to control the alarm. It has been very cool connecting the software workflow of reading the light values of the room, fetching the current weather data via the Open Weather API, and translating the text to a sound file to the physical components outputting the audio on a speaker, sounding the alarm with a buzzer, and lighting up LEDs based off data. The most difficult, yet fun, part of the project was figuring out how to connect all the code and hardware pieces. I tested all the components of the alarm separately (ie. setting off the buzzer or fetching the API data with Python), so there were some significant delays when combining them into one code file and a single circuit. It is cool to see it now with over 10 hardware components working in tandem to create a full alarm. With an annoying alarm that will certainly wake you up at the crack of dawn, people will get ahead of their day by knowing basic information such as weather before they even get out of bed. Therefore, this project is useful and can be used daily by people who would like to develop an early morning routine. The variability within when the alarm goes off based on light will give users some change day-to-day to keep the routine from getting too boring. 


## Hardware Components
- Buzzer
    - Acts as the alarm sound
- LDR and capacitor
    - The capacitor is used to build a homemade circuit to read analog values from the LDR
- LEDs
    - Simple circuits of LEDs, resistors, and GPIO pins
- JBL speaker
    - Connected to the headphone jack of the Pi


## Software Components
- Open Weather Map API
    - Used to fetch current weather data for a specific location
- Pygame library
    - The library that worked best to play sound via the Pi
- gTTs (Google Text To Speech)
    - Pre-trained AI model that converts strings of text to an mp3 file that can be played on the speaker

## Development Process
[Link to Dev Log](https://docs.google.com/document/d/102Un0wA5PAx8WMP2xizA6PiWHbftrRQiRD14P6ymWI4/edit?usp=sharing)

