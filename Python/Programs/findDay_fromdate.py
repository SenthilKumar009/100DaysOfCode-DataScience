def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year%100 == 0 and year%400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2 and isYearLeap(year):
        return 29
    else:
        return 28


def dayOfDate(year, month, date):
    monthCode = {3: 1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8, 11:9, 12:10, 1:11, 2:12}
    day = {0:'Sunday', 1:'Mondauy', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    
    #f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C
    find = date + (((13*monthCode.get(month))-1)//5) + (year%100)-1 + ((year%100)-1)//4 + ((year//100)//4) - (2*(year//100))
    #return find
    
    if find < 0:
        dayCode = find % 7 + 7
        return(day.get(dayCode))
    else:
        dayCode = find % 7
        return(day.get(dayCode))
    
print(dayOfDate(2064, 1, 29))