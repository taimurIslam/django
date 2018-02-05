import datetime
a = datetime.datetime.now()
b = datetime.datetime.now()
c = b - a
#datetime.timedelta(0, 8, 562000)
#divmod(c.days * 86400 + c.seconds, 60)
print(a)