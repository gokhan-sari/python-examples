from datetime import date

rastgele_gun = date(2021, 2, 3)
bugun = date.today()

print(bugun - rastgele_gun)
print(bugun.year)
print(bugun.month)
print(bugun.day)
print(bugun.strftime("%Y/%m/%d"))
print(bugun.strftime("%d %b %Y"))
print(bugun.strftime("%d %B %Y"))