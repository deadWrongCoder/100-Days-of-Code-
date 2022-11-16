class Question:
  def __init__(self, question, answer, number):
    self.question =  question
    self.answer = answer
    self.number = number

class Questions:
  def __init__(self):
    self.questions = [Question("The capital of Turkey is Istanbul", False, 1), Question("The last russian emperor was Nikolas II", True, 2), Question("Elvis Presley is a direct descendant of Abraham Lincoln", False, 3), Question("C Language was developed by Dennis Ritchie", True, 4)]

  def print_question(self, number):
    for question in self.questions:
      if question.number == number:
        print(question.question)

  def count_questions(self):
    return len(self.questions)

  def return_answer(self, number):
    for question in self.questions:
      if question.number == number:
        return question.answer
