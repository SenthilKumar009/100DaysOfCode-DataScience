def isPrime(num):
    flag = True
    if num == 2:
        return num
    else:
        for i in range (3, num):
            #print(i)
            if num%i == 0:
                flag = False
                break
            else:
                flag = True
        
        if flag:
            return num

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")