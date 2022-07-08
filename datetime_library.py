import datetime

start = datetime.datetime(2022, 7, 8, 16, 11)
stop = datetime.datetime(2022, 6, 8, 15, 44)
st = datetime.timedelta(weeks=10, days=3, hours=15, minutes=50, seconds=4)
sto = datetime.timedelta(days=16, hours=18, minutes=14, seconds=50)
q = str(datetime.datetime(2022, 7, 7, hour=15))
#deadline = datetime.datetime.strptime('12 5 2022', '%d %m %Y')
#print(deadline.year, deadline.month, deadline.day)

today = datetime.datetime.now()
first = datetime.datetime.now()
second = datetime.timedelta(days=1)
#print(first + second)


deadline = datetime.datetime(year=2022, month=7, day=8)


now = datetime.datetime.now()
in_two_days = datetime.timedelta(days=2)

print((now + in_two_days).year, (now + in_two_days).month, (now + in_two_days).day,  (now + in_two_days).weekday())

