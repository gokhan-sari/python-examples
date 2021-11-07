import pandas as pd
import requests

yanit = requests.get("https://www.metaweather.com/api/location/2344116/")

icerik = yanit.json()["consolidated_weather"]

df = pd.DataFrame(icerik).T #T=Transpoze
#df = df.T

print(df)
