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

#Loop for as long as the program needs to run
while programRunning:
    diceamount = input("How many dice are you rolling?")
    diceamount = int(diceamount)
    #If they type '0' for diceAmount, the loop quits immediately,
    if diceamount <= 0:
        break
    diceSides = input("How many sides does your dice have?")
    diceSides = int(diceSides)
    modifier = input("What should I add to the total result?")
    modifier = int(modifier)
    loops = diceamount
    #Rolls dice until there are no dice left to roll
    while loops > 0:
        loops -= 1
        result += random.randint(1, diceSides)
    result += modifier
    print("You rolled a total of " + str(result))
    programRunning = False
