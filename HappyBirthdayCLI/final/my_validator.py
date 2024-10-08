import re # Module for RegEx
import calendar # Module for ensuring dates entered are consistent with real dates

def validate_birthday(birthday):
    """
    Validates a birthday string in the format YYYY-MM-DD.
    
    Args:
        birthday (str): The birthday string to validate.
        
    Returns:
        str: Validation result message.
    """
    # Define a regular expression pattern to match the desired date format
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    # Check if the birthday matches the desired date format
    if not date_pattern.match(birthday):
        return "Invalid date format. Please use the format YYYY-MM-DD."

    # Split the birthday string into year, month, and day components
    year, month, day = map(int, birthday.split('-'))

    # Check if the year is within the valid range
    if year < 1900 or year > 2023:
        return "Invalid year. Please enter a year between 1900 and 2023."

    # Check if the month is within the valid range
    if month < 1 or month > 12:
        return "Invalid month. Please enter a month between 1 and 12."

    # Get the maximum number of days for the given month and year
    max_days = calendar.monthrange(year, month)[1]

    # Check if the day is within the valid range
    if day < 1 or day > max_days:
        return f"Invalid day. Please enter a day between 1 and {max_days} for the given month."

    # If all checks pass, the birthday is valid
    return "valid"
