import csv
import random


class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_user_answer(self):
        user_answer = input("")
        if user_answer == self.answer:

            print("Correct answer!!")
            return True
        else:
            print('wrong answer!!')
            return False

    def __str__(self):
        return f"Qestion No:{self.question}"


class TrueFalse(Quiz):
    """we have display method for this class to show options """

    def display_options(self, options):
        print(options)


class MultipleChoice(Quiz):
    """we have display method for this class to show options """

    def display_options(self, options):
        print(options)


class ShortAnswer(Quiz):

    def check_user_answer1(self):
        user_answer = input("").lower().lower()

        if user_answer == self.answer:

            print("Correct answer!!")
            return True
        elif user_answer != self.answer:
            print('wrong answer!!')
            return False


class UserScore:  # کلاس امتیاز
    def __init__(self, score):
        self.score = score
        self.status = "null"

    def winner_or_loser(self):
        if self.score >= 40:
            print(f" Yeeeees You Won !!! Your score is {self.score} ")
            self.status = "winner"

        else:
            print(f"Sorry You lose!!! Your score is {self.score}")
            self.status = "loser"
        return self.status


"""--------------------this function is for write on the csv file------------------------------"""


def writing_on_file(q, correct, wrong, score, remaining):
    data = [q, correct, wrong, score, remaining]
    fieldnames = ['Q', 'Correct', 'Wrong', 'Score', 'Remaining']
    with open('result.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)

        if q == 1:
            writer.writerow(fieldnames)  # اگه اولین سوال بود هم تیتر اضافه بشه به فایل هم دیتا
            writer.writerow(data)
        # csv_dict_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # csv_dict_writer.writeheader()
        # csv_dict_writer.writerow({"Q": q, "Correct": correct, 'Wrong': wrong, 'Score': score, 'Remaining': remaining})
        else:  # وقتی اولین سوال نیست به سطر ها فقط دیتا اضافه بشه

            writer.writerow(data)


"----------------this part is for Generate a random number to select questions--------------"
randomlist = []
for i in range(0, 5):
    """when i==0  I want to make sure 
    there is one  each type of question"""
    if i == 0:
        n1 = random.randint(1, 5)
        randomlist.append(n1)
        n2 = random.randint(6, 10)
        randomlist.append(n2)
        n3 = random.randint(11, 16)
        randomlist.append(n3)
        i += 3
    elif i >= 3:
        n1 = random.randint(1, 15)
        while n1 in randomlist:
            n1 = random.randint(1, 15)

        randomlist.append(n1)
print(randomlist)

"-----------------I am reading form csv file and choice 5 questions-------------------------- "
fainal_score = 0
correct_answer = 0
wrong_answer = 0
with open('new.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    for count, num in enumerate(randomlist):
        questoin_counter = 0
        fist_score = 0

        questoin_remaining = 0
        if 1 <= num <= 5:  # true and false questions are rows between 1 until 5 in csv file
            q = TrueFalse(rows[num][0], rows[num][2])  # سوال= rows[num][0], جواب=rows[num][2]

            print(q)
            q.display_options(rows[num][1])
            flag = q.check_user_answer()
            if flag:
                first_score = 10
                correct_answer += 1
                fainal_score = fainal_score + first_score

            elif flag == False:
                first_score = -3
                wrong_answer += 1
                fainal_score = fainal_score + first_score
            questoin_counter = count + 1
            questoin_remaining = 5 - questoin_counter
            writing_on_file(questoin_counter, correct_answer, wrong_answer, fainal_score, questoin_remaining)
            print(40 * "*")
            print(
                f"Q:{questoin_counter}, Correct:{correct_answer}, Wrong:{wrong_answer}, "
                f"Score:{fainal_score}, Remaining:{questoin_remaining}")


        elif 6 <= num <= 10:  # ShortAnswer question
            q1 = ShortAnswer(rows[num][0], rows[num][2])
            print(q1)
            flag2 = q1.check_user_answer1()

            if flag2:
                first_score = 10
                correct_answer += 1
                # print(first_score,correct_answer)
                fainal_score = fainal_score + first_score
            elif flag2 == False:
                first_score = -3
                wrong_answer += 1
                fainal_score = fainal_score + first_score
            questoin_counter = count + 1
            questoin_remaining = 5 - questoin_counter
            writing_on_file(questoin_counter, correct_answer, wrong_answer, fainal_score, questoin_remaining)
            print(40 * "*")
            print(
                f"Q:{questoin_counter}, Correct:{correct_answer}, Wrong:{wrong_answer}, "
                f"Score:{fainal_score}, Remaining:{questoin_remaining}")
        elif 11 <= num <= 15:  # MultipleChoice questions
            q2 = MultipleChoice(rows[num][0], rows[num][2])
            print(q2)
            q2.display_options(rows[num][1])
            flag3 = q2.check_user_answer()

            if flag3:
                first_score = 10
                correct_answer += 1
                fainal_score = fainal_score + first_score
                # print(first_score,correct_answer)
            elif flag3 == False:
                first_score = -3
                wrong_answer += 1
                fainal_score = fainal_score + first_score

            questoin_counter = count+1
            questoin_remaining = 5 - questoin_counter
            writing_on_file(questoin_counter, correct_answer, wrong_answer, fainal_score, questoin_remaining)
            print(40*"*")
            print(
                f"Q:{questoin_counter}, Correct:{correct_answer}, Wrong:{wrong_answer}, "
                f"Score:{fainal_score}, Remaining:{questoin_remaining}")
    print(40 * "*")
    result = UserScore(fainal_score)
    result.winner_or_loser()
