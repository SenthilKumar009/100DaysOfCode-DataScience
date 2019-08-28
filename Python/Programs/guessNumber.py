import random

secretNumber = random.randint(1,10)
print("I'm thinking of a Number and you guess it!!!")

for check in range(0,7):
    guess = int(input('Guess the number'))
    if(guess == secretNumber):
        print('You guessed it correct, Guessed number is', secretNumber)
        break
    elif(guess > secretNumber):
        print('Your guessing is more than the secret number, try again!')
    else:
        print('Your guessing is less than the secret number, try again!')