def leapYear(year):

    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year%100 == 0 and year%400 == 0:
        return True
    else:
        return False

print('enter the year:', end='')
year = int(input())
print(leapYear(year))