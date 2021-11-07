class ikisayi(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def toplam(self):
        return self.a + self.b


x = ikisayi(3, 5)

print(x.toplam)  # 1
print(ikisayi.toplam)  # 2
print(x.toplam())  # 3
print(ikisayi.toplam(x))  # 4
