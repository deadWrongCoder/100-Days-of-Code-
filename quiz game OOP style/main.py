from question import Question, Questions
from game_processor import Game
questions = Questions()
game = Game()

i = questions.count_questions()
while i != 0:
  questions.print_question(i)
  answer = questions.return_answer(i)
  game.check_answer(answer)
  game.print_score()
  i -= 1
