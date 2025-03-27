#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access system-specific parameters and functions

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_processor.settings')  # Set the default Django settings module
    try:
        from django.core.management import execute_from_command_line  # Import the function to execute command-line tasks
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc  # Raise an error if Django is not installed or not available
    execute_from_command_line(sys.argv)  # Execute the command-line utility with the provided arguments

if __name__ == '__main__':
    main()  # Call the main function if this script is executed directly
