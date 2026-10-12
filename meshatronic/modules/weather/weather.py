import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": -40.7549,
    "longitude": 172.8973,
    "daily": "weather_code,rain_sum",
    "timezone": "Pacific/Auckland",
}

daily = requests.get(url, params=params).json()["daily"]

wmo_codes = {
    0: "Clear",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Freezing fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Freezing drizzle",
    57: "Heavy freezing drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Light snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail",
}

for date, code, rain in zip(
    daily["time"],
    daily["weather_code"],
    daily["rain_sum"],
):
    pass
    # print(f"{date}: {wmo_codes.get(code, 'Unknown')}, {rain}mm rain")

print(daily["time"][0], wmo_codes.get(daily["weather_code"][0], "Unknown Weather"), daily["rain_sum"][0])

