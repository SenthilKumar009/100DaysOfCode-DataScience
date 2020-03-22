val = 0

def readint(prompt, min, max):
    global val 
    val = int(input(prompt))
    if val >= max or val <= -10:
        print('Error: the value is not within permitted range (-10..10)')
        readint(prompt, -10, 10)
    else:
        print(str(val))


print(readint("Enter a number from -10 to 10: ", -10, 10))

#print("The number is:", v)