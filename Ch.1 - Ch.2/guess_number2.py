##
#   18.03.08
#   20152262  Hong Geun Ji
#
#   Number guessing game.
#   Advanced version that applied while loop concept.

import random

print("Welcome to number guessing game!")

number = random.randrange(1,100)
guess = None

while number != guess:
    if(not guess):
        guess = int(input("Type the number that you can guess : "))
    else:
        print("Wrong!")
        if number > guess:
            print("The number is GREATER than you typed.\n")
            guess = int(input("Type the number that you can guess : "))
            
        else:       # Even the number and guess is same, this code will not be implemented since the while loop's boolean value is false.
            print("The number is SMALLER than you typed.\n")
            guess = int(input("Type the number that you can guess : "))


print("You're right!")
