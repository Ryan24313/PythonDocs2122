#Ryan Stevenson
#EZBank 1

#imports our custom module
import basics

#Create a new "app" and "user" object from the basics module
app = basics.newProgram()
user = basics.newUser()

#Store the user's bank balance as a property of the "user"
user.balance = 1000

#Welcome User to the Bank
print("Welcome to the Bank of Ryan")

#Loop while the app.running is True
while app.running:
    #Tell the user their balance
    print("Your Balance is $" + str(user.balance) + "\n")
    #Ask the user to select an option
    user.choice = input("1.Deposit\n2.Withdraw\n3.Exit\n\n")
    print("")
    #input() always returns a string, so compare to a string
    if user.choice == "1":
        #Ask how much they want to deposit
        user.deposit = input("How much do you want to deposit\n\n")
        print("")
        #Check to make sure the input was a Float that can be converted
        try:
            float(user.deposit)
        except ValueError:
            #Tell User they can't deposit that
            print("Your choice was invalid\n")
            user.deposit = 0
                
        if user.deposit == 0:
            user.deposit = 0
        else:
            #Add deposit
            user.deposit = float(user.deposit)
            user.balance += user.deposit
    elif user.choice == "2":
        #Ask for withdrawal amount
        user.withdraw = input("How much do you want to withdraw\n\n")
        print("")
        #Check to see if input was a number
        try:
            float(user.withdraw)
        except ValueError:
            print("Your choice was invalid\n")
            user.withdraw = 0
                
        if user.withdraw == 0:
            user.withdraw = 0
        else:
            user.withdraw = float(user.withdraw)
            if user.withdraw < user.balance:
                user.balance -= user.withdraw
            else:
                #tell user they don't have enough money
                print("Your to broke to take that much money\n")
    elif user.choice == "3":
        #Make running False so the loop does not continue
        print("Thank you for doing buisness at the Bank of Ryan")
        app.running = False
    else:
        print("Your choice was invalid\n")
