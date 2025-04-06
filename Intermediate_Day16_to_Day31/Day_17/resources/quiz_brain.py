# TODO asking questions
# TODO checking is ans is correct
# TODO checking if it is end of quiz


class QuizBrain:
    def __init__(self, question):
        self.question_number = 0
        self.questions_list = question
        self.score = 0
        
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q. {self.question_number} {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Check if the docstring still has questions left
        """
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False
        # return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_answer, current_answer):
        if current_answer.lower() == user_answer.lower():
            print(f"You got it right!!")
            self.score += 1
        else:
            print(f"That is wrong")

        print(f"The correct answer was: {current_answer}")
        print(f"You're current score is : {self.score} / {self.question_number}")
        print("")