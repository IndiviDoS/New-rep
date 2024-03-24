import datetime
x = datetime.datetime.now()
print(f"{x.year}.{x.month}.{x.day-5} {x.hour}.{x.minute}.{x.second}")

import datetime
x = datetime.datetime.now()
print(f"{x.year}.{x.month}.{x.day-1}")
print(f"{x.year}.{x.month}.{x.day}")
print(f"{x.year}.{x.month}.{x.day+1}")

import datetime
x = datetime.datetime.now()
print(f"{x.strftime("%Y.%m.%d %H:%M:%S")}")

import datetime
x = datetime.datetime.now()
z = x.timestamp()
y = input("input date")
y = datetime.strptime(y,"%Y.%m.%d")
o = y.timestamp()
print(abs(z - o))