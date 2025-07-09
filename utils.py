import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city: str, units: str = "metric") -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": units}
    response = requests.get(base_url, params=params)

    print("Weather API URL:", response.url)
    print("Weather Status:", response.status_code)

    if response.status_code != 200:
        print("Weather API Error:", response.text)
        return {"error": "City not found or API error"}

    try:
        return response.json()
    except Exception as e:
        print("JSON Decode Error:", e)
        return {"error": "Weather response not in JSON format."}


def get_forecast_data(lat: float, lon: float, units: str = "metric") -> list:
    # Use One Call v2.5 (free-tier compatible)
    url = "https://api.openweathermap.org/data/2.5/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "current,minutely,hourly,alerts",
        "units": units,
        "appid": API_KEY
    }

    response = requests.get(url, params=params)
    print("Forecast API URL:", response.url)
    print("Forecast Status:", response.status_code)

    if response.status_code != 200:
        print("Forecast API Error:", response.text)
        return []

    try:
        data = response.json()
        return data.get("daily", [])
    except Exception as e:
        print("Forecast JSON Decode Error:", e)
        return []

