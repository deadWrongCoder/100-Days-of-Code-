print("Welcome to the Password Generator! ")
n_letters = int(input("How many letters would you like? " ))
n_numbers = int(input("How many numbers would you like? " ))
n_symbols = int(input("How many symbols would you like? " ))
password = []
for i in range(0, n_letters):
  password.append(random.choice(stuff.letters))

for i in range(0, n_numbers):
  password.append(random.choice(stuff.numbers))

for i in range(0, n_symbols):
  password.append(random.choice(stuff.symbols))
  
random.shuffle(password)
password_as_string = "".join(password)
print(f"{password_as_string}")
  
