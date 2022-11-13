import random

names = input("Type all the names divided by a comma and a space. ").split(", ")
length = len(names)
print(names[random.randint(0, length - 1)] + " is going to pay the total bill! ")
