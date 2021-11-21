from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


class Card:
    def __init__(self, balance):
        self.balance = balance
        self.trip = 0
        self.p_trip = 2000

    def number_of_trip(self):  # calculat with this credit how many trip you can go price of each trip is 2000
        self.trip = int(self.balance) // self.p_trip

    def use_card(self):  # this method up date the balance after each use of the card
        if self.balance >= 2000:
            self.balance = self.balance - self.p_trip
            self.trip -= 1
            print("your balance:", self.balance)
            print("Have a good trip")

        elif self.balance < 2000:
            print("balance of card not enough!!!")

    def __str__(self):
        return f"credit of card :{self.balance}, number of trip: {self.trip}"

    def __repr__(self):
        return f"balance :{self.balance}, number of trip: {self.trip}"


class SingleTrip(Card):  # کارت تک سفره
    counter = 0

    def __init__(self, balance):
        super().__init__(balance)

        SingleTrip.counter += 1
        self.id = str(SingleTrip.counter) + "singletrip"

    def __str__(self):
        return f"credit of card :{self.balance}, number of trip: {self.trip},id:{self.id}"

    def __repr__(self):
        return f"balance :{self.balance}, number of trip: {self.trip},id:{self.id}"


class Credit(Card):  # کارت اعتباری
    counter = 0

    def __init__(self, balance):
        super().__init__(balance)
        Credit.counter += 1
        self.id = str(Credit.counter) + "credit"

    @classmethod
    def charge(cls):

        number = input("Specify the number of trips")
        new_balance = int(number) * 2000

        check = input(f"price of {number} trip is {new_balance} enter yes or no :").upper()
        if check == "YES":
            cls.balance = new_balance
            cls.trip = number
            print("charge succesfully")

            return cls.balance
        elif check == "NO":
            print("Failed to increase credit")

    def __str__(self):
        return f"credit of card :{self.balance}, number of trip: {self.trip},id:{self.id}"

    def __repr__(self):
        return f"balance :{self.balance}, number of trip: {self.trip},id:{self.id}"


class TimeCredit(Credit):  # کارت اعتباری زمانی
    counter = 0

    def __init__(self, balance):
        super().__init__(balance)
        TimeCredit.counter += 1
        self.id = str(TimeCredit.counter) + "timecredit"

    def calculate_exp(self):
        self.today = date.today()
        # print(today)
        self.exp = date.today() + relativedelta(months=+2)  # exp of each car is 2 month ago
        # print(self.exp)

    def use_card(self):  # this method up date the balance after each use of the card
        if self.balance >= 2000 and str(self.exp) > str(self.today):
            self.balance = self.balance - self.p_trip
            self.trip -= 1
            print("your balance:", self.balance)
            print("Have a good trip")

        elif self.balance < 2000:
            print("balance of card not enough!!!")
        elif str(self.exp) < str(self.today):
            print("exp of card finished!!!")

    def __str__(self):
        return f"credit of card :{self.balance}, number of trip: {self.trip},id:{self.id,},exp_card:{self.exp}"

    def __repr__(self):
        return f"balance :{self.balance}, number of trip: {self.trip},id:{self.id},exp_card:{self.exp}"


"""--------------------------------this part is for by and charge card--------------------------------------"""
singeltrip_list = []
credit_list = []
time_credit_list = []
while True:
    print("wich one of the cards do you want:")
    type_card = input("  1:singl trip , 2:Credit , 3:Time credit ,4:cancle:")
    if type_card == '1':
        print("The cost of each single trip card is 2000 toman!!")
        y_n = input("enter yes or no :").upper()
        if y_n == "YES":
            trip1 = SingleTrip(2000)
            trip1.balance
            trip1.number_of_trip()
            singeltrip_list.append(trip1)
            print("you should keep this cod and use it to trip--> ", trip1.id)
            print(singeltrip_list)
        elif y_n == "NO":
            print("you enter NO so you don't by any card!!!")

    elif type_card == '2':
        print("you should first charge your card:")
        b = Credit.charge()
        trip2 = Credit(b)
        print(trip2.balance)
        trip2.number_of_trip()
        credit_list.append(trip2)
        print("you should keep this cod and use it to trip -->", trip2.id)
        print(credit_list)

    elif type_card == '3':
        print("you should first charge your card:")
        t = TimeCredit.charge()
        trip3 = TimeCredit(t)
        print(trip3.balance)
        trip3.number_of_trip()
        trip3.calculate_exp()
        time_credit_list.append(trip3)
        print("you should keep this cod and use it to trip -->", trip3.id)
        print(time_credit_list)
    elif type_card == '4':
        break


"""-------------------------------this part is for use to trip card------------------------------------"""
print("if you buy card say me which one of them do you want to use:")
while True:
    kind_trip = input("1:singl trip , 2:Credit , 3:Time credit ,4:cancle")
    if kind_trip == '1':  # trip by single trip card:
        check_idcard = input("enter your card's code to check:")
        for s_card in singeltrip_list:
            if check_idcard in s_card.id:
                s_card.use_card()

            else:
                print("Please get a subway card first ")

    elif kind_trip == '2':  # trip by credit card
        check_idcard = input("enter your card's code to check:")
        for credit_card in credit_list:  # هر عضو این لیست یک شی از کلاس کارت اعتباری است
            if check_idcard in credit_card.id:
                credit_card.use_card()

            else:
                print("Please get a subway card first ")
    elif kind_trip == '3':
        check_idcard = input("enter your card's code to check:")
        for tcredit_card in time_credit_list:  # هر عضو این لیست یک شی از کلاس کارت اعتباری زمانی است
            if check_idcard in tcredit_card.id:
                tcredit_card.use_card()

            else:
                print("Please get a subway card first ")
    elif kind_trip == '4':
        break
