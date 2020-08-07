from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

"""DATETIME CALCULATIONS USING TIMEDELTA OBJECTS
Timedelta is a class from the datetime module used for a span of time and date. It allows you to perform time-based calculations







"""
# Part two   34
# Part Three {a practical frequently used method}  46
# 
# 
# 
# 
# 
# 
# today = datetime.now()

# print(today)  # 2020-08-06 19:57:46.530980

# print(str(today + timedelta(365)))  # 2021-08-07 09:54:25.594652

# print(timedelta(days=365,hours=7,minutes=5))  # 365 days, 7:05:00



# Part two
today = datetime.now()

print(str(today + timedelta(days=4,weeks=5)))  # 2020-09-15 10:09:25.866767

x = datetime.now() - timedelta(weeks=2)
y = x.strftime("%A %B %d, %Y")

print(y)  # Friday July 24, 2020



# Part Three

daysAhead = date.today()

xmas = date(daysAhead.year,12,25)

timetoexmas = xmas - daysAhead

print("It is just",timetoexmas.days, "days to Christmas 2020")  # It is just 140 days to Christmas 2020

