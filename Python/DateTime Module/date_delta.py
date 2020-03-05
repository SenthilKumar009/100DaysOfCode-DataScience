import datetime

today = datetime.date.today()
tdelta = datetime.timedelta(days=7)

print(today + tdelta)

bday = datetime.date(2020, 5, 19)

print('My Birthday will be in {} days!!!'.format(bday-today))