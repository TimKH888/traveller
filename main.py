import requests


city_info_headers = {
    'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
    'x-rapidapi-key': "d4670f4573mshca492fc0bd3310ap11c9a1jsn2c70ee09337e"
}


def getCityIdAndPhoto(c_name):
    city_id_url = f"https://tripadvisor1.p.rapidapi.com/locations/search"
    city_info_query = {"query": c_name}
    city_id_response = requests.request("GET", city_id_url, headers=city_info_headers, params=city_info_query)
    if city_id_response.json()["data"][0]["result_type"] == "geos":
        c_id = city_id_response.json()["data"][0]["result_object"]["location_id"]
        c_photo_link = city_id_response.json()["data"][0]["result_object"]["photo"]["images"]["original"]["url"]
        return c_id, c_photo_link
    else:
        print("There is no information for this city\n")
        mainMenu()


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


def getCityRestaurants(c_id):
    city_restaurants_url = "https://tripadvisor1.p.rapidapi.com/restaurants/list"
    city_restaurants_query = {"location_id": c_id}
    city_restaurants_response = requests.request("GET", city_restaurants_url, headers=city_info_headers,
                                                 params=city_restaurants_query)
    c_restaurants = []
    for restaurant in city_restaurants_response.json()["data"]:
        if "name" in restaurant.keys():
            c_restaurants.append({
                "name": restaurant["name"],
                "number_of_reviews": restaurant["num_reviews"],
                "photo": restaurant["photo"]["images"]["original"]["url"],
                "rating": restaurant["rating"],
                "description": restaurant["description"],
                "web_site_url": restaurant["web_url"]
            })
    return c_restaurants


def mainMenu():
    city_name = input("Enter a city name or \"exit\": ").strip().lower()
    if city_name == "exit":
        exit()
    else:
        print("Loading...\n")
        city_id, city_photo_link = getCityIdAndPhoto(city_name)
        cityMenu(city_name, city_id, city_photo_link)


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
        print(f"The photo of the city: {c_photo_link}\n")
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
        city_restaurants = getCityRestaurants(c_id)
        print("The list of restaurants in this city:")
        for restaurant in city_restaurants:
            print("Name: " + restaurant["name"] + "\n"
                  "Number of reviews: " + str(restaurant["number_of_reviews"]) + "\n"
                  "Photo: " + restaurant["photo"] + "\n"
                  "Rating: " + str(restaurant["rating"]) + "\n"
                  "Description: " + restaurant["description"] + "\n"
                  "Web site: " + restaurant["web_site_url"] + "\n")
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