from Sign_in import signin
from Sign_up import signup, database
import atm



tries = 0 #counts how many times the user failed to log in
online_user = None

print("~Welcome to Python Bank~")
while True:
    
    try:
        account = int(input("1: Sign up \n2: Sign in \n3: Exit \n"))
    except ValueError:
        continue
    
    if account == 2:
        username = signin()
        if username:
            online_user = username
            break
        else:
            tries += 1 
            if tries == 3:
                print("Too many failed attempts.")
                exit() #exits program if user failed to log in 3 times in a row
    elif account == 1:
        signup()
    elif account == 3:
        exit()
    else:
        print("No such option")

#creating a user after the online user does a successfull sign in
main_user = atm.ATM(online_user)
print("What would you like to do")
print("--------------------------")

while True:
    try:
        choices = int(input("""
                        1: Check Balance
                        2: Withdraw
                        3: Deposit
                        4: Exit\n"""))
    except ValueError:
        print("Please type the correct choice") #error handling if input is not an integer

    if choices == 1:
        print(f"{main_user.user}, your current balance is {main_user.balance} €")#shows the users balance from the ATM class

    elif choices == 2:
        amount = float(input("Enter amount to withdraw: "))
        main_user.withdraw(amount) #withdraw method from ATM class

    elif choices ==3:
        amount = float(input("Enter amount to deposit: "))
        main_user.deposit(amount) #deposit method from ATM class

    elif choices == 4:
        break #exits the loop but not the program

    else:
        print("No such choice") #error handling if input is not 1-4




