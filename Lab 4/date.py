#1 
import datetime 
x = datetime.datetime.now() 
print(f"{x.year}.{x.month}.{x.day-5} {x.hour}:{x.minute}:{x.second}") 

#2
import datetime
x = datetime.datetime.now()
print(f"{x.year}.{x.month}.{x.day-1}")
print(f"{x.year}.{x.month}.{x.day}")
print(f"{x.year}.{x.month}.{x.day+1}")

#3
import datetime
x = datetime.datetime.now()
print(f"{x.strftime("%Y.%m.%d %H:%M:%S")}")

#4 
import datetime 
x = datetime.datetime.now() 
x_seconds = x.timestamp() 
any_data = datetime.datetime(2024,2,16,10,12,10) 
any_data_seconds = any_data.timestamp() 
print(abs(x_seconds - any_data_seconds))
