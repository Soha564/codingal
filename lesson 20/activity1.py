from datetime import date, time, datetime

today = date.today()
print(today)

current_date = datetime.now()
print(current_date)

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

print(time(11, 34, 56))

import calendar

print(calendar.calendar(theyear=2025))
print(calendar.month(2025, 4))


c = calendar.Calendar()
print("Iter weekdays:", list(c.iterweekdays())) # 0 - Monday, 6 - Sunday

print("Iter monthdays:", list(c.itermonthdays(2025, 4)))

print("Month Dates Calendar:", list(c.monthdatescalendar(2025,10)))

print("Month Days 2 Calendar:", list(c.monthdays2calendar(2025, 11)))

print("Month Days Calendar:", list(c.monthdayscalendar(2025,11)))