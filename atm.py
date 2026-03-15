from Sign_up import database

class ATM:
    def __init__(self, user):
        self.balance = database[user]["balance"] #takes the users balance from the db
        self.user = user
       

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money
        database[self.user]["balance"] = self.balance  #updates the db   

    def deposit(self, money):
        self.balance += money
        database[self.user]["balance"] = self.balance   #updates the db  
