import requests

yanit = requests.get(
    "https://www.metaweather.com/api/location/search/?query=istanbul")

print(yanit.json())

sehir_adi = yanit.json()[0]["title"]
print(sehir_adi)

sehir_id = yanit.json()[0]["woeid"]
print(sehir_id)
