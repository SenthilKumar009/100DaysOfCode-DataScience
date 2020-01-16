# write your function here
def readable_timedelta(days):
    if days % 7 == 0:
        total_weeks = days / 7
        return str(int(total_weeks)) + " week(s) and 0 day(s)"
    else:
        total_weeks = days / 7
        total_days = days % 7
        return str(int(total_weeks)) + " week(s) and " + str(total_days) + " day(s)."

# test your function
print(readable_timedelta(7))