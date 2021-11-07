import pandas as pd

sutunlar = [
    "ID", "TARIH", "ZAMAN", "LAT", "LONG", "ULKE", "SEHIR", "BOLGE", "YON",
    "MESAFE", "DERINLIK", "XM", "MD", "BUYUKLUK", "MW", "MS", "MB"
]

df = pd.read_csv("deprem.csv", sep=",", skiprows=1, names=sutunlar)

print(df[df["BUYUKLUK"] != 0].head(60))
