katilimci1 = "Ozdemir, Nida"
katilimci2 = "Yildiz, Samet"
katilimci_listesi = [katilimci1, katilimci2]


def katilimci_adi_ayikla(katilimci):
    ad = katilimci.split(", ")[1]
    soyad = katilimci.split(", ")[0]
    return ad, soyad


def tesekkur_mesaji_hazirla(katilimci):
    ad, soyad = katilimci_adi_ayikla(katilimci)
    tesekkur_mesaji = "Sayin {} {}, katiliminiz icin tesekkur ederiz.".format(ad, soyad.upper())
    print(tesekkur_mesaji)


for katilimci in katilimci_listesi:
    tesekkur_mesaji_hazirla(katilimci)
