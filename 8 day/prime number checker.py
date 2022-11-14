def prime_or_not(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime == True:
    print("It's a prime number")
  else:
    print("It's not a prime number")
    
    

print("Welcome to the Prime number checker! ")
number = int(input("Type a number: "))
prime_or_not(number)
