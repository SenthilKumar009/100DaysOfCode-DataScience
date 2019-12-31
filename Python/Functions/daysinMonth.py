month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 !=0 or year %400 == 0)

def days_in_month(year, month):

    if month < 1 or month > 12:
        return 'Invalid Month'

    if month == 2 and isLeapYear(year):
        return 29
    else:
        return month_days[month]

print(days_in_month(2021, 2))
