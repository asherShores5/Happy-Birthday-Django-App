import logging # logs to 'birthday.log'
from datetime import datetime # date/time object
from my_validator import validate_birthday as vb # my validator module



class Birthday:
    # Sets up Birthday class.
    # Steps chain together within each function.

    def __init__(self):
        self.birthday = None # Sets default birthday value

    def get_birthday(self):
        # Prompt the user to enter their birthday and validate the input.
        self.birthday = input("Please enter your birthday (YYYY-MM-DD): ")

        # Validate the user's input
        validation_result = vb(self.birthday)

        if validation_result == "valid":
            logging.info("Valid birthday provided.")
            self.check_if_birthday()
        else:
            logging.error(f"Invalid birthday provided: {validation_result}")
            print(f"Invalid birthday provided: {validation_result}")

    def check_if_birthday(self):
        # Check if today is the user's birthday based on the entered birthday.
        today = datetime.now().date().strftime("%m-%d") 
        birthday_date = datetime.strptime(self.birthday, "%Y-%m-%d").date().strftime("%m-%d") # Formats month and day only

        if today == birthday_date:
            logging.info("Today is the user's birthday.")
            print("Happy birthday! Today is your special day!")
        else:
            logging.info("Today is not the user's birthday.")
            print("Today is not your birthday, but have a great day!")
        # Logs and displays info to user regarding birthday

        self.calculate_age() # Continues to find age of user

    def calculate_age(self):
        # Calculate the user's age based on the entered birthday.
        today = datetime.now().date() # Gets todays date
        birthday = datetime.strptime(self.birthday, "%Y-%m-%d").date() # Gets date of birth
        age = today.year - birthday.year # Calculates age

        if today < birthday.replace(year=today.year):
            age -= 1 # Subtracts year from age if birthday has not occured this year

        logging.info(f"User's age calculated: {age}")
        print(f"You are {age} years old.")
        # Prints and logs current age value


