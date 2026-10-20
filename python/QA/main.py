from question_model import Quetion
from data import question_data
from quiz_brain import QuizBrain

quetion_bank=[]
for quetion in quetion_data:
  question_text=question['text']
  question_answer=question['answer']
  new_question=Question(question_text,question_answer)
  question_banl.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()


  
