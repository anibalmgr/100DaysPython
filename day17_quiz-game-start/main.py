from data2 import data_2
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in data_2:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your score final score is {quiz.score}/{len(question_bank)}")
