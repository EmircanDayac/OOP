class QuizBrain:


    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list



    def nextQuestion(self):
        Score = 0

        istrue = True
        while istrue:
            current_question = self.question_list[self.question_number].text
            print(f"S/{self.question_number} Question : {current_question} True/False?")
            current_respon = input()
            print(self.question_list[self.question_number].Answer)
            if self.question_list[self.question_number].Answer == current_respon:
                self.question_number +=1

                Score +=10
                print(f"You own score :{Score}")
            else:
                istrue = False








