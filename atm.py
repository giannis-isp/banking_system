from Sign_up import database

class ATM:
    def __init__(self, user):
        self.balance = database[user]["balance"]
        self.user = user
        print(f"{user}, your current balance is {database[user]["balance"]} €")

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money

    def deposit(self, money):
        self.balance += money