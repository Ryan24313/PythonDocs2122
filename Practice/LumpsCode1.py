#Lump
#Random Dice Generator
#For Dungeons & Dragons and other nerd stuff

#imports the random module
import random

#Sets up the variables we will use in this program
diceAmount = 1
diceSides = 6
modifier = 0
programRunning = True
result = 0

#I forget what this next line does:
while programRunning:
    diceamount = input("How many dice are you rolling? ")
    diceamount = int(diceamount)
    #If they type '0' for diceAmount, the loop should quit immediately, but I forget how
    #Use 'break' to stop a loop immeidately
    diceSides = input("How many sides does your dice have? ")
    diceSides = int(diceSides)
    modifier = input("What should I add to the total result?")
    modifier = int(modifier)
    loops = diceamount
    #I forget what this does:
    while loops > 0:
        loops -= 1
        result += random.randint(1, diceSides)
    results += modifier
