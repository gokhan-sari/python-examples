import requests

yanit = requests.get("https://www.metaweather.com/api/location/2344116/")

print(yanit.json())
