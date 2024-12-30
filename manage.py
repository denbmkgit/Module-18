#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()





'''
django-admin startproject myapp


django-admin startproject UrbanDjango


python manage.py runserver

python manage.py startapp app

python manage.py startapp example1

python manage.py startapp example2

python manage.py startapp example3

pip freeze | Out-File -Encoding UTF8 requirements.txt
'''