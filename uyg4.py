sayilar = list(range(5))


def karesini_al(x):
    return x**2


sayilar_yeni = []

for sayi in sayilar:
    sayilar_yeni.append(karesini_al(sayi))

print(sayilar_yeni)
