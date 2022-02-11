import random

upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCaseLetters = upperCaseLetters.lower()
digits = "0123456789"
symbols = "~`!@#$%^&*()_-+={[}]|\\\:;""'<,>.?/"""
all = upperCaseLetters + lowerCaseLetters + digits + symbols

length = int(input("Length of the password: "))
quantity = int(input("Quantity: "))

for i in range(quantity):
    password = "".join(random.sample(all, length))
    print("Password [" + str(i+1) + "]: ", password)