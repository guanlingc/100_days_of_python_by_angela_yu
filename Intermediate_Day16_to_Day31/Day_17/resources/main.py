from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data:
    question = Question(i['text'],i['answer'])
    question_bank.append(question)

quiz= QuizBrain(question_bank)
continue_game = True

while continue_game:
    quiz.next_question()
    quiz.still_has_questions()


print(f"You've completed the quiz")
print(f"Your final score was {quiz.score} / {len(question_bank)}")