class Game:
  def __init__(self):
    self.user_score = 0

  def check_answer(self, answer):
    user_answer = int(input("Is that true of false? Type 1 or 0 "))
    if (user_answer == 1 and answer == True) or (user_answer == 0 and answer == False):
      self.user_score += 1  
      
  def print_score(self):
    print("Current score is ", self.user_score)
