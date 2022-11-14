import random
import click

def refresh():
  click.clear() 
  print("Welcome to the Hangman Game!")
  print(f"You have {attempts} attempts.")
  print("The word is ", ("").join(printed_word))

def check_game_state():
  if attempts == 0:
    print("You lose")
    return True
  for i in range(0, len(printed_word)):
    if printed_word[i] == '*':
      return False
  print("You won")    
  return True    
def check_similar_letters(guess):
  for i in range(0, len(hidden_word) - 1):
    if hidden_word[i] == guess:
      printed_word[i] = guess
  
  
words = ["python", "developer", "snake"]
game_is_over = False
print("Welcome to the Hangman Game! ")
hidden_word = random.choice(words)
attempts = 10
print(f"You have {attempts} attempts.")
printed_word = []
for i in range(0, len(hidden_word)):
  printed_word.append("*")
  
print("The word is ", ("").join(printed_word))

while not game_is_over:
  guess = input("Type a letter: ")
  for i in range(0, len(hidden_word)):
    if guess == hidden_word[i]:
      printed_word[i] = guess
      check_similar_letters(guess)
      refresh()
      game_is_over = check_game_state()
      break
    elif i == len(hidden_word) - 1:
      attempts -= 1
      refresh()
      game_is_over = check_game_state()
