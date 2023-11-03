
from data import question_data

class QuestionM:
    def __init__(self):
        for i in range(len(question_data)):
            self.text = question_data[i]["text"]
            self.answer = question_data[i]["answer"]
            print(f"Question {i+1}: {self.text}")
            self.inp = input()
            if self.inp == self.answer or self.inp == self.answer.lower():
                self.score()
                print(f"Correct.\nCurrent score: {self.net_score}/{len(question_data)}")
            else:
                print(f"Incorrect.\nCorrect answer was: {self.answer}\nCurrent score: {self.net_score}/{len(question_data)}")

        if self.net_score == 12:
            print("Congrats. You have answered all questions correctly and have scored 12/12!")
        else:
            if self.net_score<=5:
                print(f"Your score is quite low. Try next time.")
            elif 5<self.net_score<10:
                print(f"Your score is quite good. Maybe play again to see if you score more.")
            else:
                print("You have a great score.")

    net_score = 0
    def score(self):
        self.net_score += 1

q = QuestionM()


