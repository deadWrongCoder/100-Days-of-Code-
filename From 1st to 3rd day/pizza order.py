'''
Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

'''

size = input("What size of pizza do you prefer? Type S, M or L: ").upper()
price = 0
if size == 'S':
  price = 15
elif size == 'M':
  price = 20
else:
  price = 25
pepperoni = input("Do you want to add some pepperoni? Type Y or N. ").upper()

cheese = input("Do you want to add some cheese? Type Y or N.").upper()


if pepperoni == "Y":
  if size == "S":
    price +=2
  else:
    price +=3
if cheese == 'Y':
  price +=1

print(f"Your total bill is ${price}")  
