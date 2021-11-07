#print("deneme")

#x = input("deger girin")

#if x == "5":
#    print(("helal be!"))

from os import replace
from tqdm import tqdm
import time

dosya = "şifredosyası.txt"
menu = ""
while menu not in ["1", "2", "3", "4"]:
    print(
        """Welcome to password manager app. Which action would you like to do?
1. View old passwords
2. Create a new password
3. Close the app""")
    menu = input("")
    if menu == "1":
        for i in tqdm(range(100)):
            time.sleep(0.01)
        try:
            şifredosyası = open('şifredosyası.txt', "r")
            for i in şifredosyası:
                data = i.split("\n")
                print(data[0])
            print("\nThese are your old passwords. Wanna go back to menu?")
            evetyadahayır1 = input("")
            menu = evetyadahayır1.lower()
            if menu not in ["yes", "sure", "okay", "okey", "ok"]:
                quit()
        except FileNotFoundError:
            print(
                "File can not be found. You have to create a new one. For that, i gonna re-open the app.\n"
            )
            time.sleep(2)
            menu = ""
    if menu == "2":
        şifre = input("Please enter your new password: ")
        şifredosyası = "şifredosyası.txt"
        şifredosyası = open("şifredosyası.txt", "a")
        şifredosyası.write(şifre + "\n")
        şifredosyası.close()
        for i in tqdm(range(100)):
            time.sleep(0.01)
        print("Your password is successfully saved. Wanna go back to menu?")
        evetyadahayır1 = input("")
        menu = evetyadahayır1.lower()
        if menu not in ["yes", "sure", "okay", "okey", "ok"]:
            quit()
    if menu == "3":
        print("""Thank you for testing my application!
Badge received: Quest is Over""")
        quit()
    if menu == "4":  #bunu bilmen gerekmiyor
        print("\nBadge received: How did we get here?")
