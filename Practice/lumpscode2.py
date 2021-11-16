'''
hello im lump how are you i am a hanzo main.
im learning computer programming but my
doctor says i have a mediccal condtion called
"dumm" this program makes you guess a number
and u get so many guesses. i forget how to
program tho becuse of my conditon. if you
help me i will give you 19 vbucks.
'''
import random

guess=0
number=0
loops=3

number = random.randint(1, 10)
while loops > 0: #Loop 3 times
    guess = input("Guess a number\n")
    print("")
    if guess.isdecimal() and int(guess) > 0:
        guess = int(guess)
        if guess > number:
            print("You guessed too high\n")
            loops -= 1
        elif guess < number:
            print("You guessed too low\n")
            loops -= 1
        elif guess == number:
            print("You guessed correctly!\n")
            loops = 0
    else:
        print("You did not guess a number")
