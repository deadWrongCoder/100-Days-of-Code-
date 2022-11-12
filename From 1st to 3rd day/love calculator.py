def count_letters(name1, name2, letter):
  return name1.count(letter) + name2.count(letter)

print("Welcome to the Love Calculator!")
name1 = input("What's your name? ").lower()
name2 = input("What's their name? ").lower()
true = "true"
love = "love"
true_number = 0
love_number = 0
for letter in true:
  true_number += count_letters(name1, name2, letter)
for letter in love:
  love_number += count_letters(name1, name2, letter)
print(f"Your chances are {true_number}{love_number} %.")
  
