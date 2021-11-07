sayilar = list(range(1, 10))


def cift_sayi_dondur(x):
    if x % 2 == 0:
        return x
    else:
        return None


sayilar_yeni = []

for sayi in sayilar:
    if cift_sayi_dondur(sayi) is not None:
        sayilar_yeni.append(cift_sayi_dondur(sayi))

print(sayilar_yeni)
