import random
import ascii

computer_choices = [0, 1, 2]
arts = [ascii.Rock, ascii.Scissors, ascii.Paper]
player_choice = int(input("Type 0 for Rock, 1 for Scissors, 2 for Paper: "))
computer_choice = random.choice(computer_choices)
print(f"You chose: {arts[player_choice]}")
print(f"Computer chose: {arts[computer_choice]}")

if computer_choice == player_choice:
  print("It`s draw!")
elif (computer_choice == 0 and player_choice == 1) or  (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 0):
  print("You lose")
else:
  print("You win")
