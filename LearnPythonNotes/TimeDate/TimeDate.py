from datetime import date
from datetime import time
from datetime import datetime
'''DATE TIME
    FORMATTING DATE
strtime()  the method used to format the date time objects into readable strings.
The datetime object has a method for formating date objects into readable strings. It is called strtime()
Directive   Description                             Example
%a          Weekday short version                   Mon
%A          Weekcay full version                    Monday
%w        Weekday index numbers 0-6:Mon is index 0  0
%d          Day of Month:01-31                      17
%b          Month name short version                Dec
%B          Month name full version                 April
%m          Month as a number : 01 - 12             12
%y          Year short version, without century     20
%Y          Year long version                       2020


    FORMATTING TIME
Directive   Description                                         Example
%H      Hour : 00 - 23                                          18
%I      Hour : 00 = 12                                          07
%p      AM | PM                                                 AM
%M      Minute : 00 - 59                                        47
%S      Seconds: 00 - 58                                        07
%f      Microsecond : 000000 -999999                            656789
%z      UTC offset                                              + 0100  ???? space
%Z      Timezone                                                CST
%J      Day number of yrar : 001 - 366                          365
%U      Week number of year. Sunday as first day of week. 00-53     52
%W      Week number of year. Monday as first day of week. 00-53     52
%c      Local version of date and time                          Mon Apr 8 13:05:00 2019
%x      Local version of date                                   04|8|19
%X      Local version of time                                   14:20:00
%%      A % character                                           %

The datetime object has a method for formatint date objecte into readable strings. It is called strftime()
It takes one parameter, format to specify the format of the Returned string.




'''
# Part Two   63
# Part Three Using the date time constructor   71
# Formatting Date and Time  81
# Formatting Local Time  part Three   93
# 
# 
# 
# 
# 
# 
# today = date.today()  # comennet out for Part three

# print('Today is ', today)  # Today is  2020-08-06

# print("The date components are ", today.day,today.month,today.year)  # The date components are  6 8 2020



# Part Two
# print("the weekday number is", today.weekday())  # the weekday number is 3

# days = ['mon', 'tues', 'wed','thu','fri','sat','sun']
# print('the weekday is', days[today.weekday()])  # the weekday is thu  ** the day of the week that I did this lesson.



# Part 3 Using the date time constructor
# today = datetime.now()

# print("The current time is ", today)  # The current time is  2020-08-06 15:28:55.462147

# t = datetime.time(datetime.now())
# print("The time now is ", t)



# Formatting Date and Time  part Two
# today = datetime.now()

# # print(today)  # 2020-08-06 17:37:04.482915

# # print(today.strftime('the current year is: %Y'))  # 2020

# print(today.strftime("%a,%d %B, %y"))  # Thu,06 August, 20



# Formatting Local Time  part Three
today = datetime.now()

print(today.strftime('%c'))  # Thu Aug  6 18:06:02 2020

print(today.strftime('%x'))  # 08/06/20

print(today.strftime("%X"))  # 18:11:13

print(today.strftime("%I:%M:%S %p"))  # 06:15:14 PM

print(today.strftime("%I:%M"))  # 06:18
