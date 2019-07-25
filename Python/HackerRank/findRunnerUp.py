totalInput = int(input('Enter the total number of Scores:'))
myList = list()
for i in range(0,totalInput):
    myList.append(int(input()))

nums = sorted(list(set(myList)))[-2]

print('Runner Up Score is:', nums)
