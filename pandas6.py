import pandas as pd

sutunlar = [
    "ID", "TARIH", "ZAMAN", "LAT", "LONG", "ULKE", "SEHIR", "BOLGE", "YON",
    "MESAFE", "DERINLIK", "XM", "MD", "BUYUKLUK", "MW", "MS", "MB"
]

df = pd.read_csv("deprem.csv", sep=",", skiprows=1, names=sutunlar)

df.drop(labels=["ID", "XM", "MD", "MW", "MS", "MB"], axis=1, inplace=True)

df["BOLGE"] = df["BOLGE"].str.replace("_", " ")

df = df[df["BUYUKLUK"] != 0].reset_index(drop=True)

df["CIDDIYET"] = "COK YUKSEK"
df.loc[df["BUYUKLUK"] < 5.5, "CIDDIYET"] = "YUKSEK"
df.loc[df["BUYUKLUK"] < 4.5, "CIDDIYET"] = "DUSUK"
df.loc[df["BUYUKLUK"] < 3.5, "CIDDIYET"] = "ONEMSIZ"

df.info()  #veritabaninin bilgilerini goster
#df = df.sort_values(by="BUYUKLUK", ascending=False).reset_index(drop=True)     #deprem buyuklugunu buyukten kucuge sirala
print(df.head(60))
print(df["CIDDIYET"].value_counts())  #ciddiyet sutunu ekle
print(df.groupby("ULKE").mean())  #ulkelere gore kumele
print(df.groupby(["ULKE",
                  "SEHIR"]).mean().head(60))  #ulke ve sehirlere gore kumele
print(df.groupby(["ULKE", "SEHIR"])["BUYUKLUK"].mean().nlargest(
    5))  #ulke ve sehirlere gore en buyukleri 5'i getir
