print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
#If the user does not guess the correct answer, enter the loop
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
#ask the user fo a guess    
    if int(guess) == number:
#is the guess a correct number?        
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
#if the correct guess,tell the user it was the correct guess and exit the loop
#if the wrong guess, tell the user it was the wrong guess and continue he loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess)) 