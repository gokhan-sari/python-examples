class Account:
    def __init__(self, isim, numara, bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print("Isim: ", self.isim)
        print("Hesap No: ", self.numara)
        print("Bakiye: ", self.bakiye)

    def paraCek(self, miktar):
        if (self.bakiye < miktar):
            print("Bakiye yetersiz!")
        else:
            self.bakiye -= miktar
            print("Kalan Bakiye: ", self.bakiye)

    def paraYatir(self, miktar):
        self.bakiye += miktar
        print("Yeni Bakiye: ", self.bakiye)


hesap = Account("Ali Can", 123, 10000)

hesap.hesapBilgileri()
hesap.paraCek(500)
hesap.paraYatir(1000)
