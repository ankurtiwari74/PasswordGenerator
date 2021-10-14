import random
import string

print("Hello, Welcome to Password Generator!")

length = int(input("Please enter the length of your password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

all_characters = lower + upper + number + symbol

temp = random.sample(all_characters, length)

password = "".join(temp)

print(password)
