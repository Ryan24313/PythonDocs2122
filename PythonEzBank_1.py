#Ryan Stevenson
#EZBank 1
import basics
app = basics.newProgram()

user = basics.newUser()
app.running = True
app.balance = 1000

while app.running == True:
    print("Your Balance is $" + str(app.balance) + "\n")
    user.choice = input("1.Deposit\n2.Withdraw\n3.Exit\n\n")
    print("")
    if user.choice == "1":
        user.deposit = input("How much do you want to deposit\n\n")
        print("")
        if user.deposit.isdecimal() == True:
            user.deposit = int(user.deposit)
            app.balance += user.deposit
        else:
            print("Your choice was invalid\n")
    elif user.choice == "2":
        user.withdraw = input("How much do you want to withdraw\n\n")
        print("")
        if user.withdraw.isdecimal() == True:
            user.withdraw = int(user.withdraw)
            if user.withdraw < app.balance:
                app.balance -= user.withdraw
            else:
                print("You don't have enough money\n")
        else:
            print("Your choice was invalid\n")
    elif user.choice == "3":
        app.running = False
    else:
        print("Your choice was invalid\n")
