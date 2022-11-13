import random
import click
def main_loop():
  print("Welcome to Find a Treasure!\n ")
  row_1 = ["[ ]","[ ]","[ ]"]
  row_2 = ["[ ]","[ ]","[ ]"]
  row_3 = ["[ ]","[ ]","[ ]"]
  map =[row_1, row_2, row_3]
  print((" ").join(row_1))
  print((" ").join(row_2))
  print((" ").join(row_3))
  treasure = [random.randint(0,2), random.randint(0,2)]
  player_guess = []
  player_guess= input("Where's a treasure? Let's find out. Type the coordinates divided by a comma and a space. ").split(", ")
  for i in range(0, len(player_guess)):
    player_guess[i] = int(player_guess[i])
  if treasure[0] == player_guess[0] and treasure[1] == player_guess[1]:
    map[player_guess[0]] [player_guess[1]] = '0'
    click.clear()
    print("Welcome to Find a Treasure!\n ")
    print((" ").join(row_1))
    print((" ").join(row_2))
    print((" ").join(row_3))
    print("You found the treasure! ")
  else:
    map[player_guess[0]][player_guess[1]] = '[X]'
    click.clear()
    print("Welcome to Find a Treasure!\n ")
    print((" ").join(row_1))
    print((" ").join(row_2))
    print((" ").join(row_3))
    print("There's no treasure here! ")
 

main_loop()
