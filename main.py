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


def mainMenu():
    city_name = input("Enter a city name or \"exit\": ").strip().lower()
    if city_name == "exit":
        exit()
    else:
        print("Loading...\n")
        cityMenu(city_name, 0, "0")


def cityMenu(c_name, c_id, c_photo_link):
    print("Options:\n"
          "-City photo\n"
          "-Weather\n"
          "-Restaurants\n"
          "-Attractions\n"
          "-Hotels\n"
          "-Back")
    option = input("Enter an option: ").strip().lower()
    print()
    if option == "city photo":
        cityMenu(c_name, c_id, c_photo_link)
    elif option == "weather":
        print("Loading...\n")
        city_weather_info = getWeatherInfo(c_name)
        print("Weather information:\n"
              "Weather: " + city_weather_info["weather_type"] + "\n"
              "Temperature: " + str(city_weather_info["temperature"]) + "\n"
              "Temperature feels like: " + str(city_weather_info["temperature_feels_like"]) + "\n"
              "Pressure: " + str(city_weather_info["pressure"]) + "\n"
              "Humidity: " + str(city_weather_info["humidity"]) + "\n")
        cityMenu(c_name, c_id, c_photo_link)
    elif option == "restaurants":
        print("Loading...\n")
        cityMenu(c_name, c_id, c_photo_link)
    elif option == "attractions":
        print("Loading...\n")
        cityMenu(c_name, c_id, c_photo_link)
    elif option == "hotels":
        print("Loading...\n")
        cityMenu(c_name, c_id, c_photo_link)
    elif option == "back":
        mainMenu()
    else:
        print("There is no such option\n")
        cityMenu(c_name, c_id, c_photo_link)


mainMenu()
