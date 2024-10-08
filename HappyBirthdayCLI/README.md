Happy Birthday Python Program

1. The program should output a prompt to the user asking what day their birthday is.
2. The program should read the user's input
3. The program should be able to tell if today is the user's birthday
4. The program should output a message telling the user if today is their birthday
    a. Output the age of the user
5. The program should use an __init__() method
6. The program should be composed of multiple modules (files)
7. The program should have meaningful code comments
8. The program should have logging to a file
    a. The logging should be meaningful 
9. The program should validate input birthday data
    a. The program should have appropriate outputs telling the user why the data they input was wrong and how they could fix it


Notes:
Created basic script implementations in Tester dir.
birthday_basic.py includes the basic functionality. Does not have any checks for user input error and does not include anything beyond step 4.

birthday_advanced.py has a really poorly developed input validation
Made it more complex than I needed to because I wanted to give specific advice to user on how to input their birthdate correctly.

main.py and myHelper.py was just experimenting with modules and making sure they were working. 
Solution explained below, but could not get attributes in my modules to work for a while.

Final program included in final dir.

Had a bug that kept saying that the helper module my_validation had no attributes.
Eventually realized that it was because I had not enabled autosave so the main script was reading the file as empty.

Isolated 'my_birthday.py' to handle birthday class and associated functions.
Main is mostly empty now.
'my_validator.py' handles birthday validation on its own since that is a key part of the program. 
Implemented calendar module in addition to regular datetime RegEx logic.