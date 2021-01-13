# This program makes you guess the number betwwen 1 and 10

import random

print("This program makes you guess the number betwwen 1 and 10\n")
# Generates random numbers between 1 and 10
num = random.randint(1,10)

while True:
    guessNum = int(input("Guess a number betweeen 1 and 10: "))

    if guessNum < num:
        print("too low") # prints if the guess is too low
    elif guessNum > num:
        print("too high") # prints if the guess is too high
    else:
        print("You guessed it!") # prints if the player guessed the number
        break
