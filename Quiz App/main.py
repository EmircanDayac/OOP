from data import  question_data
from question_model import   Question

question_bank= []
for i in question_data:
    question_text = i["text"]
    question_answer = i["text"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


print(question_bank[0])
