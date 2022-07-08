import calendar

dec = calendar.TextCalendar(firstweekday=0)

cal = [i for i in calendar.month_abbr]

for i in cal:
    print(i)