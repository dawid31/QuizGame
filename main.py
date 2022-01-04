from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
quesiton_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    quesiton_bank.append(new_question)


quiz = QuizBrain(quesiton_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.still_has_questions()
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")


