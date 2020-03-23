def digitLife(dob):
    sum = total = 0
    for ch in dob:
        total += int(ch)
    
    while total > 0:
        #total = total%10
        sum = sum + total%10
        total = int(total/10)
    return sum

print(digitLife('20170101'))
print(digitLife('20202103'))
print(digitLife('19991229'))