from random import choice

characters = "abcdefghijklmnopstuvwxyz0123456789"

password = ""

for index in range(8):
    password += choice(characters)

print(password)
