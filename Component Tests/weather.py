import requests
import datetime

# Replace YOUR_API_KEY with your actual API key
api_key = 'f95cf4e0206468f647dd9c15d5092f6e'

# Replace CITY_NAME with the name of the city you want to get weather info for
city = 'Davidson'

# Set up the API URL
url = f'https://api.openweathermap.org/data/2.5/weather?lat=35.4993&lon=-80.8487&appid={api_key}'
# https://api.openweathermap.org/data/2.5/weather?lat=35.4993&lon=80.8487&appid=f95cf4e0206468f647dd9c15d50

# Send the HTTP request and receive the response
response = requests.get(url)

# Parse the JSON response data into a Python dictionary
data = response.json()

print(data)

temperature = round((int(data['main']['temp']) - 273.15) * 1.8 + 32, 0)
description = data['weather'][0]['description']

weather_text = f'The temperature in {city} is {temperature} degrees Fahrenheit and the weather is {description}'
print(weather_text)

sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
print(sunrise)
sunrise = sunrise + datetime.timedelta(minutes=15)
print(sunrise)
#def calc_hours_past_sunrise(sunrise):
