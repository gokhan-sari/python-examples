from tkinter import *

arayuz = Tk()

arayuz.title("Arayuz Uygulamasi")
arayuz.geometry("500x300")

etiket = Label(arayuz, text="Merhaba")
etiket.grid(column=1, row=0)


def tiklama():
    global etiket
    etiket.configure(text="Dugmeye Tiklandi!")


dugme = Button(arayuz, text="Dugmeye Bas!", command=tiklama)
dugme.grid(column=2, row=1)

arayuz.mainloop()
