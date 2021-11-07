import random


def random_liste_olustur(random_boyutu, liste_boyutu):
    liste = []
    for k in range(0, liste_boyutu):
        rand = random.randint(0, random_boyutu)
        liste.append(rand)
    return (liste)


def liste_bubble_sirala(liste):
    for j in range(0, len(liste) - 1):
        for i in range(0, len(liste) - 1):
            if liste[i] > liste[i + 1]:
                temp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = temp
    return (liste)


liste = random_liste_olustur(100, 100)
print(liste)

liste = liste_bubble_sirala(liste)
print(liste)

#with open("file.txt", 'w+') as file_handler:
#    for item in liste:
#        file_handler.write("{}, ".format(item))
