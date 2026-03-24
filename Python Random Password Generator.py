import random
import string
print("Welcome to password generator")
name = input("Username: ")
length = int(input("How long do you want? "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
allchar = lower+upper+digit
password = [random.choice(lower),random.choice(upper),random.choice(digit)]
for i in range(length-3):
    password.append(random.choice(allchar))
password = "".join(password)
print(f"Hi {name}, your password is {password}")