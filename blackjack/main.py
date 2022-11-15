import random
import click
cards = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
dealer_deck = []
player_deck = []
is_game_over = False
def generate_cards():
  dealer_deck.append(cards[random.randint(0, 12)])
  dealer_deck.append(cards[random.randint(0, 12)])
  player_deck.append(cards[random.randint(0, 12)])
  player_deck.append(cards[random.randint(0, 12)])

def display_cards(is_game_over):
  if is_game_over == False:
    print(f"Your cards are {player_deck}")
    print(f"The first dealer's card is {dealer_deck[0]}")
  else:
    print(f"Your cards are {player_deck}")
    print(f"Dealer'cards are {dealer_deck}")
    
def hit():
  player_deck.append(cards[random.randint(0, 12)])  
  
def question(player_sum, is_game_over):
  answer = int(input("Do you wanna hit or stand. 1 or 0 "))
  if answer == 1:
    hit()
    count_cards(is_game_over)
  else:
    sum = 0
    for card in dealer_deck:
      sum += card
    if 11 in dealer_deck and sum > 21:
      sum -= 10
    if sum > 21:
      is_game_over = True
      click.clear()
      display_cards(is_game_over)
      print("Player won.")
    elif sum == 21:
      is_game_over = True
      click.clear()
      display_cards(is_game_over)
      print("Dealer have a BlackJack. You lose")
    elif sum <=21 or sum > 17:
      if player_sum > sum:
        is_game_over = True
        click.clear()
        display_cards(is_game_over)
        print("Player won")
      else:
        is_game_over = True
        click.clear()
        display_cards(is_game_over)
        print("Dealer won")
    elif sum < 17:
      dealer_deck.append(cards[random.randint(0, 12)])
      count_cards(is_game_over)
              
def count_cards(is_game_over):
  sum = 0
  for card in player_deck:
    sum += card
  if 11 in player_deck and sum > 21:
    sum -= 10
  if sum < 21:
    click.clear()
    display_cards(is_game_over)
    question(sum, is_game_over)
  elif sum == 21:
    is_game_over = True
    click.clear()
    display_cards(is_game_over)
    print("You have a BlackJack! You won.")
  else:
    is_game_over = True
    click.clear()
    display_cards(is_game_over)
    print("You have a Bust. You lose.")

generate_cards()
display_cards(is_game_over)
count_cards(is_game_over)
