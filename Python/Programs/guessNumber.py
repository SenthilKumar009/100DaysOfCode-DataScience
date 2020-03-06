import random

secretNumber = random.randint(1,10)
print("I'm thinking of a Number and you guess it!!!")

for check in range(0,3):
    guess = int(input('Guess the number:'))
    
    if(guess == secretNumber):
        print('You guessed it correct, you guessed my secrect number in ' + str(check+1) + ' guesses!!!')
        break
    elif(guess > secretNumber):
        if check == 3:
            print('Your guessing limit is over. The secrect Number is ' +secretNumber)
        else:
            print('Your guessing is more than the secret number, try again!')
    else:
        if check == 2:
            print('Your guessing limit is over')
        else:
            print('Your guessing is less than the secret number, try again!')