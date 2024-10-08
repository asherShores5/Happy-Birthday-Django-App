#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def is_conda_env():
    return os.path.exists(os.path.join(sys.prefix, 'conda-meta'))

def main():
    """Run administrative tasks."""
    if not is_conda_env():
        print("Warning: Not running in a Conda environment. Some features may not work as expected.")
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HappyBirthdaySite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment or Conda environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()