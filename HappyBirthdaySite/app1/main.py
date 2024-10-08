import logging # logs to 'birthday.log'
import my_birthday as mb # sets up birthday class

logging.basicConfig(
    # Logging file basic config
    filename='birthday.log', # Ensures 'birthday.log' exists
    level=logging.INFO, # Sets basic format
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__": # Ensures file runs only if main
    logging.info("Program started.") # Logs to file
    birthday = mb.Birthday() # Creates instance of birthday class from 'my_birthday.py'
    while(True):
        birthday.get_birthday()
        goAgain = input("Would you like to go again? (y/n)\n")
        if(goAgain == 'y' or goAgain == 'Y'):
            continue
        else:
            exit()