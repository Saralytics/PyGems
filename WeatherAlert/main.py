import requests
import os
from dotenv import load_dotenv

weather_url = "https://api.openweathermap.org/data/2.5/weather"
forcast_url = "https://api.openweathermap.org/data/2.5/forecast"
load_dotenv()
appid = os.getenv("API_KEY")
print(appid)

parameters = {
    "q": "Beijing",
    "appid": appid,
    "cnt": 4
}

# Weather codes: https://openweathermap.org/weather-conditions
# For each of the 4 timewindows(the next 12 hours), if any main code less than 7, we should bring an umbrella

response = requests.get(url=forcast_url, params=parameters)
response.raise_for_status()
data = response.json()['list']

will_rain = False
for hour_data in data:
    weather_code = hour_data['weather'][0]['id']
    if weather_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
