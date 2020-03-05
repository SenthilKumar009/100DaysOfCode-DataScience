import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'January 01, 1987'

print(datetime.datetime.strptime(dt_str, '%B %d, %Y'))