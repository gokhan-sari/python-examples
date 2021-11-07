import requests

yanit = requests.get("https://www.metaweather.com/api/location/2344116/")

print(yanit.json())

print(yanit.json()["consolidated_weather"][0]["the_temp"])
print(yanit.json()["consolidated_weather"][0]["weather_state_name"])
