from datetime import date


class Insan():
    def __init__(self, isim, telefon_numarasi, dogum_tarihi):
        self.isim = isim
        self.telefon_numarasi = telefon_numarasi
        self.dogum_tarihi = dogum_tarihi

    def yas_hesapla(self):
        guncel_yil = date.today()
        return (guncel_yil - self.dogum_tarihi).days // 365


class Ogrenci(Insan):
    def __init__(self, isim, telefon_numarasi, dogum_tarihi, ogrenci_no,
                 transkript):
        super().__init__(isim, telefon_numarasi, dogum_tarihi)
        self.ogrenci_no = ogrenci_no
        self.transkript = transkript

    def not_ortalamasi_hesapla(self):
        return 4


insan1 = Insan("Ahmet", "0212 945 38 17", date(1990, 8, 19))
insan1.yas_hesapla()
insan2 = Insan("Ekin", "0252 363 11 10", date(2000, 3, 9))
insan2.yas_hesapla()
insan3 = Insan("Güler", "0535 402 18 72", date(1970, 11, 20))
insan3.yas_hesapla()

ogrenci1 = Ogrenci("Ahmet", "0545 715 65 45", date(1995, 5, 18), 419, [])
ogrenci1.yas_hesapla()
ogrenci1.not_ortalamasi_hesapla()

print(insan1.yas_hesapla())
print(insan2.yas_hesapla())
print(insan3.yas_hesapla())

print(ogrenci1.yas_hesapla())
print(ogrenci1.not_ortalamasi_hesapla())
