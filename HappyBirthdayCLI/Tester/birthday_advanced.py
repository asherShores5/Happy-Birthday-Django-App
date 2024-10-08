# More advanced functionality
# Includes input validation

from datetime import date, datetime

def validate_input(dob):
    flag = False
    year = dob[0:4]
    month = dob[5:7]
    day = dob[8:10]

    if not (year.isnumeric()):
        print("You have entered in your year of birth incorrectly. Try something like '1987' or '2000.'")
        return True
    year = int(year)
    if (dob[4:5] != '-'):
        print("You have entered in your year of birth incorrectly. Try something like '1987' or '2000.'")
        return True
    if not (month.isnumeric()):
        print("You have entered in your month of birth incorrectly. Try something like '04' if you were born in April or '12' if you were born in December.")
        return True
    elif (int(month) < 1 or int(month) > 12):
        print("You have entered in a month value out of range. There are only 12 months in the year so your response must range from 1 to 12.")
        return True
    year = int(year)
    if not (day.isnumeric()):
        print("You have entered in your day of birth incorrectly. Try something like '17' if you were born on the 17th or '22' if you were born on the 22nd.")
        return True
    elif (int(day) < 1):
        print("You have entered in your day of birth incorrectly. Your response must be greater than 0.")
        return True
    elif (month == "02" and int(day) > 29):
        print("You have entered in your day of birth incorrectly. If you were born in February, your day of birth cannot exceed 29")
        return True
    elif ((month == "09" or month == "04" or month == "06" or month == "11") and int(day) > 30):
        print("You have entered in your day of birth incorrectly. Based on your given birth month your day of birth cannot exceed 30.")
        return True
    elif (int(day) > 31):
        print("You have entered in your day of birth incorrectly. Based on your given birth month your day of birth cannot exceed 31.")
        return True

    return flag



# Driver Code

def main():
    #saves today's date in var today
    today = str(date.today())

    while(True):
        #Ask for date in same format as datetime lib
        print("Please enter your birthday in the format yyyy-mm-dd")
        bday = input() # save user input to input var
        flag = validate_input(bday)
        if (flag == False):
            break

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

    print("Would you like to go again? (y/n)")
    runAgain = input()
    if (runAgain == 'y'):
        main()
    else:
        quit()
    
main()