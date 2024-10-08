from django.shortcuts import render
from .models import Birthday
import re
import calendar
from datetime import datetime

def validate_birthday(birthday):
    """
    Validates a birthday string in the format YYYY-MM-DD.
    
    Args:
        birthday (str): The birthday string to validate.
        
    Returns:
        dict: Validation result dictionary.
    """
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    
    if not date_pattern.match(birthday):
        return {'valid': False, 'error_message': "Invalid date format. Please use the format YYYY-MM-DD."}

    year, month, day = map(int, birthday.split('-'))

        # Get the current year
    current_year = datetime.now().year
    
    if year < 1900 or year > current_year:
        return {'valid': False, 'error_message': f"Invalid year. Please enter a year between 1900 and {current_year}."}

    if month < 1 or month > 12:
        return {'valid': False, 'error_message': "Invalid month. Please enter a month between 1 and 12."}

    max_days = calendar.monthrange(year, month)[1]

    if day < 1 or day > max_days:
        return {'valid': False, 'error_message': f"Invalid day. Please enter a day between 1 and {max_days} for the given month."}

    birthday_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    today = datetime.now().date().strftime("%m-%d")
    if today == birthday_date.strftime("%m-%d"):
        message = "Happy birthday! Today is your special day!"
    else:
        message = "Today is not your birthday, but have a great day!"

    age = calculate_age(birthday_date)

    return {'valid': True, 'message': message, 'age': age, 'birthday_date': birthday_date}


def calculate_age(birthday):
    today = datetime.now().date()
    age = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1

    return age


def your_view(request):
    if request.method == 'POST':
        birthday = request.POST.get('birthday')

        validation_result = validate_birthday(birthday)
        if validation_result['valid']:  # Use integer index instead of string index
            birthday_entry = Birthday.objects.create(birthday_date=validation_result['birthday_date'])
            birthday_entry.save()

            message = validation_result['message']
            age = validation_result['age']
            return render(request, 'your_template.html', {'message': message, 'age': age})
        else:
            error_message = validation_result['error_message']
            return render(request, 'your_template.html', {'error_message': error_message})

    return render(request, 'your_template.html')

