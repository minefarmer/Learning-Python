import calendar




'''WORKING WITH CALENDERS








'''
# Plain text calender   26
# HTML Calender   43
# Looping through the calender using the for loop   62
# Using locale   105
# Part 3 Day of week for meeting   137
# 
# 
# 
# 
# 
# Plain text calender   ****   using a class called TextCalendar
# cal = calendar.TextCalendar(calendar.SUNDAY)

# str = cal.formatmonth(2020,8)

# print(str)  #     August 2020
#             # Su Mo Tu We Th Fr Sa
#             #                 1
#             # 2  3  4  5  6  7  8
#             # 9 10 11 12 13 14 15
#             # 16 17 18 19 20 21 22
#             # 23 24 25 26 27 28 29
#             # 30 31




# HTML Calender
# cal = calendar.HTMLCalendar(calendar.SUNDAY)

# str = cal.formatmonth(2020,8)

# print(str)  # <table border="0" cellpadding="0" cellspacing="0" class="month">
#             # <tr><th colspan="7" class="month">August 2020</th></tr>
#             # <tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
#             # <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sat">1</td></tr>
#             # <tr><td class="sun">2</td><td class="mon">3</td><td class="tue">4</td><td class="wed">5</td><td class="thu">6</td><td class="fri">7</td><td class="sat">8</td></tr>
#             # <tr><td class="sun">9</td><td class="mon">10</td><td class="tue">11</td><td class="wed">12</td><td class="thu">13</td><td class="fri">14</td><td class="sat">15</td></tr>
#             # <tr><td class="sun">16</td><td class="mon">17</td><td class="tue">18</td><td class="wed">19</td><td class="thu">20</td><td class="fri">21</td><td class="sat">22</td></tr>
#             # <tr><td class="sun">23</td><td class="mon">24</td><td class="tue">25</td><td class="wed">26</td><td class="thu">27</td><td class="fri">28</td><td class="sat">29</td></tr>
#             # <tr><td class="sun">30</td><td class="mon">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
#             # </table>




# Looping through the calender using the for loop
# cal = calendar.TextCalendar(calendar.SUNDAY)

# for days in cal.itermonthdays(2020,7):
#     print(days)  # 0
                # 0
                # 0
                # 1
                # 2
                # 3
                # 4
                # 5
                # 6
                # 7
                # 8
                # 9
                # 10
                # 11
                # 12
                # 13
                # 14
                # 15
                # 16
                # 17
                # 18
                # 19
                # 20
                # 21
                # 22
                # 23
                # 24
                # 25
                # 26
                # 27
                # 28
                # 29
                # 30
                # 31
                # 0
                
                
                
                
# Using locale
# cal = calendar.TextCalendar(calendar.SUNDAY)

# for days in cal.itermonthdays(2020,7):
#     print(days)
    
# for name in calendar.month_name:
    # print(name)  # January
                # February
                # March
                # April
                # May
                # June
                # July
                # August
                # September
                # October
                # November
                # December
                
# for day in calendar.day_name:
#     print(day)  # Monday
                # Tuesday
                # Wednesday
                # Thursday
                # Friday
                # Saturday
                # Sunday
                
                
                

# Part 3 Day of week for meeting
print("Team meeting will be on :")

for m in range(1,13):
    cal = calendar.monthcalendar(2020,m)  # the monthcalendar function returns an array of weeks that represent the month
    wk1 = cal[0]
    wk2 = cal[1]
    
    if wk1[calendar.FRIDAY] != 0:
        meeting = wk1[calendar.FRIDAY]
    else:
        meeting = wk2[calendar.FRIDAY]
    print("%10s %d"  % (calendar.month_name[m], meeting))  #    January 3
                                                                # February 7
                                                                #     March 6
                                                                #     April 3
                                                                #     May 1
                                                                #     June 5
                                                                #     July 3
                                                                #     August 7
                                                                # September 4
                                                                # October 2
                                                                # November 6
                                                                # December 4
    