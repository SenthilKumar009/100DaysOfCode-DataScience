def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(num):
    if (num >=13 and num <= 14) or (num>16 and num<20):
        return 0
    else:
        return num

print(no_teen_sum(1,13,15))