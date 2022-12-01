import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    password = []
    for i in range(0, random.randint(8, 13)):
        password.append(random.choice(letters))

    for i in range(0, random.randint(3, 7)):
        password.append(random.choice(numbers))

    for i in range(0, random.randint(2, 5)):
        password.append(random.choice(symbols))

    random.shuffle(password)
    password_as_string = "".join(password)
    return password_as_string
