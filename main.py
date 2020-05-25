import requests


def getWeatherInfo(c_name):
    weather_key = "9a65d9b34d2d2d7041856453c1c7c505"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={c_name}&appid={weather_key}"
    weather_response = requests.request("GET", weather_url)
    weather_info = {
        "weather_type": weather_response.json()["weather"][0]["main"],
        "temperature": weather_response.json()["main"]["temp"],
        "temperature_feels_like": weather_response.json()["main"]["feels_like"],
        "pressure": weather_response.json()["main"]["pressure"],
        "humidity": weather_response.json()["main"]["humidity"]
    }
    return weather_info


print(getWeatherInfo("moscow"))
