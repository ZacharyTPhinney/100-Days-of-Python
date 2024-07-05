from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for item in question_data:
  question = item["text"]
  answer = item["answer"]
  new_question= Question(question,answer)
  question_bank.append(new_question)

quiz = Quizbrain(question_bank)


while quiz.still_has_questions():
  quiz.next_question()
