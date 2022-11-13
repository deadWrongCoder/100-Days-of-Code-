import random

names = input("Type the names divided by a comma and a space. ").split(", ")
print(random.choice(names) + " is going to pay the total bill! ")
