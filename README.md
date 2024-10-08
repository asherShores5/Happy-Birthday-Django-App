# Birthday Checker

Birthday Checker is a project that includes both a Django web application and a simple Python CLI tool. Both versions determine a user's age and check if today is their birthday based on their provided date of birth.

## Features

- Accepts a well-formatted date of birth (YYYY-MM-DD)
- Calculates the user's current age
- Determines if today is the user's birthday
- Validates date inputs using Python's calendar library to ensure correctness for:

    - 30/31 days in a given month
    - Leap year calculations (consistent with the Gregorian calendar)



## Versions

### Web Application

- Backend: Django (Python)
- Frontend: HTML, CSS

### CLI Tool

- Simple Python script for command-line usage

Technical Stack

- Python
- Django (for web version)
- Python's datetime and calendar libraries

## Setup and Installation

### Web Application

1. Clone the repository:

```bash
git clone https://github.com/asherShores5/Happy-Birthday-Django-App
cd birthday-checker
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open your browser and navigate to http://localhost:8000 to use the application.

### CLI Tool

1. Navigate to the CLI tool directory:

```bash
cd HappyBirthdayCLI/final/
```

2. Run the script:

```bash
python main.py
```

## Usage

### Web Application

1. Enter your date of birth in the format YYYY-MM-DD.
2. Click the "Submit" button.
3. The application will display your current age and whether today is your birthday.

### CLI Tool

1. Run the script and follow the prompts to enter your date of birth.
2. The tool will display your current age and whether today is your birthday.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.