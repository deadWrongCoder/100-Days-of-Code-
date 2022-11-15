import random
import click
billionares = {
  "Elon Musk": 219,
  "Jeff Bezos": 171,
  "Bill Gates": 129,
  "Warren Buffet": 118,
  "Larry Page": 111,
  "Sergey Brin": 107,
  "Michael Bloomberg": 82,
  "Mark Zuckerberg": 37
}

def game():
  score = 0
  def random_person():
    person = random.choice(list(billionares))
    return person
  def display(person1, person2):
    print(f"1. {person1} or  2.{person2}")
  def not_the_same(person1, person2):
    while person1 == person2:
      person2 = random_person()
    return person2  

  def check_answer(person1, person2, score):
    guess = int(input("Who is more wealthier? 1 or 2? "))
    if billionares[person1] > billionares[person2] and guess == 1:
      score += 1
      person1 = person2
      person2 = not_the_same(person1, person2)
      display(person1, person2)
      check_answer(person1, person2, score)
    elif billionares[person1] < billionares[person2] and guess == 2:
      score += 1
      person1 = person2
      person2 = not_the_same(person1, person2)
      display(person1, person2)
      check_answer(person1, person2, score)
    else:
      print(f"Your score is {score}")

  person1 = random_person()
  person2 = person1
  person2 = not_the_same(person1, person2)
  display(person1, person2)
  check_answer(person1, person2, score)

game()
    
