import click

auctions = {}
def auction():
  is_over = 0
  while is_over != 1:
    name = input("What's your name? ")
    price = int(input("What's your bid? "))
    auctions[name] = price
    is_over = int(input("Are there any bidders? Type 0 for yes, 1 for no: "))
    if is_over == 0:
      click.clear()
    
def choose_winner():
  max = 0
  winner = ""
  for name in auctions:
    price = auctions[name]
    if price > max:
      max = price
      winner = name
  return name

auction()
name = choose_winner()
print(name, " wins with the bid of ", auctions[name])
