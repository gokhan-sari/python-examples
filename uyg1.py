sayilar = [5, 2, 1, 9, 8, 6, 4, 7, -1]
minimum = sayilar[0]

for sayi in sayilar[1:]:
    if sayi < minimum:
        minimum = sayi

print(minimum)
