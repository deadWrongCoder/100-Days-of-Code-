import random
import click

def game():
  
  def generate_number():
    return random.randint(1, 100)

  def choose_mode():
    mode = int(input("Choose a mode: hard or easy. Type 1 or 0: "))
    if mode == 1:
      return 5
    else:
      return 10
  def type_score(lifes):
    
    print(f"You have {lifes} attempts.")

  def guessing(number, lifes):
    guess = int(input("What's your guess? "))
    if guess == number and lifes > 0:
      print(f"You guessed the number. The number is {number}")
      game()
    elif guess > number and lifes > 0:
      print("The number is lower than your guess. Try again")
      lifes -= 1
      type_score(lifes)
      guessing(number, lifes)
    elif guess < number and lifes > 0:
      print("The number is higher than your guess. Try again")
      lifes -= 1
      type_score(lifes)
      guessing(number, lifes)
    else:
      print("You lose")
      game()
      
      
    
  print("Welcome to the Number Guessing Game! ")  
  number = generate_number()
  lifes = choose_mode()
  type_score(lifes)
  guessing(number, lifes)
  
game()
