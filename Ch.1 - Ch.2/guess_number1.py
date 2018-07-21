##
#   18.03.08
#   20152262  Hong Geun Ji
#
#   Number guessing game.

print("Welcome to number guessing game!")
number = 62
guess = int(input("Type the number that you can guess : "))

if number == guess:
    print("You're right!")
else:
    print("You're worng!")

print("Game OVER")
