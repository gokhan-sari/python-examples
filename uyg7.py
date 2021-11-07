#import datetime

#bugun = datetime.date.today()
#print(bugun)

from datetime import date

bugun = date.today()

print(bugun)
print(date.fromordinal(737425))
print(date.fromisoformat("2020-10-10"))
print(date.fromisocalendar(2020, 52, 5))
