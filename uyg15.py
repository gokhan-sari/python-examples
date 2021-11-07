# ax^2 + bx + c


def kokBul(a, b, c):
    delta = (b**2 - 4 * a * c)
    if (delta < 0):
        print("Reel Kok Yok!")
        return

    x1 = (-b - delta**0.5) / (2 * a)
    x2 = (-b + delta**0.5) / (2 * a)
    print(x1, x2)


kokBul(3, 5, 2)
