#Ryan
#Practice Using expression and conditonal statements

#An expression is a problem that must be solved
#5 + 5 is "arithmetic" expression
x = 5 + 5

#Fumctions/methods must be resolved as expressions as well
answer = input("What is your name?")

#Comparison expression resolve as Ture/False
print(7>7)
print(7>=7)
print(x==10)
print(x>10 or x<10)

#A conditional statements run if its condition is Ture / not False
if answer == "Bob":
    print("Hello, Bob! Welcome Bob!")
    print("This line also prints if your name is Bob")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("Sorry, I only talk to Bobs")
print("This line isn't inside of the if statement, and prints regardless")

# ^ If checks a condition
# ^ Elif checks a condition if the previous condions were not Ture
# ^ You can have as meny elif's as you want
# ^ Else runs if no prior conditions were true
