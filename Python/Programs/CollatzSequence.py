def collatz(number):
    if number % 2 == 0:
        print(number/2)
    else:
        print(number * 3 + 1)

collatz(3)
collatz(4)