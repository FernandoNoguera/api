import requests

def get_city_weather(city_name):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID=f736811e918ca981c13e61311f520686"
    ).json()
    return response

def get_forecast(city_name):
    forecast = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&cnt=7&APPID=f736811e918ca981c13e61311f520686"
    ).json()
    return forecast
        