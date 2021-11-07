from tkinter import *
from datetime import date
import random
import requests

arayuz = Tk()

arayuz.title("Hava Durumu")
arayuz.geometry("400x150")

etiket = Label(arayuz, text="Sehir Ismi Giriniz")
etiket.grid(column=0, row=0)

sehir = Entry(arayuz)
sehir.grid(column=1, row=0)


def rastgele_tarih_olustur():
    rastgele_yil = random.randint(2019, 2020)
    rastgele_ay = random.randint(1, 12)
    rastgele_gun = random.randint(1, 30)
    rastgele_tarih = date(rastgele_yil, rastgele_ay, rastgele_gun)
    return rastgele_tarih.strftime("%Y/%m/%d")


def sehir_konumu_bul():
    global sehir
    yanit = requests.get(
        "https://www.metaweather.com/api/location/search/?query={}".format(
            sehir.get()))
    sehir_id = yanit.json()[0]["woeid"]
    return sehir_id


def hava_durumu_bul():
    global sehir
    sehir_id = sehir_konumu_bul()
    rastgele_tarih = rastgele_tarih_olustur()
    yanit = requests.get(
        "https://www.metaweather.com/api/location/{}/{}/".format(
            sehir_id, rastgele_tarih))
    print("Sehir: {}\nTarih: {}\nDerece: {}\nHava Durumu: {}".format(
        sehir.get(), rastgele_tarih,
        yanit.json()[0]["the_temp"],
        yanit.json()[0]["weather_state_name"]))


dugme = Button(arayuz, text="Havayi Goster", command=hava_durumu_bul)
dugme.grid(column=1, row=1)

arayuz.mainloop()
