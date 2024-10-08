# Basic functionality only
# Can do steps 1-4

from datetime import date, datetime

#saves today's date in var today
today = str(date.today())

#Ask for date in same format as datetime lib
print("Please enter your birthday in the format yyyy-mm-dd")
bday = input() # save user input to input var

if (bday[-5:] == today[-5:]):
    print("Happy Birthday!")
else:
    print("Today is not your birthday")

# convert string to date object
d1 = datetime.strptime(bday, "%Y-%m-%d")
d2 = datetime.strptime(today, "%Y-%m-%d")

# difference between dates in timedelta
delta = d2 - d1
age_in_years = delta.days // 365
print(f"You are {age_in_years} years old")
