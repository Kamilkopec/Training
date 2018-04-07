# print 'today is {day}, month day, year

import datetime
import calendar

days = list(calendar.day_name)
months = list(calendar.month_name)
timetuple = datetime.date.timetuple(datetime.date.today())
tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = timetuple

print("Today is {}, {}, {}, {}".format(days[tm_wday], months[tm_mon], tm_mday, tm_year))

# from udemyu

print(datetime.datetime.now().strftime('Today is %A, %B %d, %Y'))
