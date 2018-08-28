#!/usr/bin/env python
import os
import sys


# python manage.py migrate
# Open up the urls.py file inside the inner nanaapp folder
# create a file called urls.py in ieltsapp for HomePageView/AboutPageView/ReadingPageView
# create views.py in ieltsapp to create views from templates
# create templates index.html, about.html
# python -m django --version
# django-admin startproject kenapps
# django-admin startproject hudaapp
# python manage.py makemigrations ieltsapp  if you change your model
# python manage.py sqlmigrate ieltsapp 0003
# python manage.py migrate
# python manage.py shell
# python manage.py showmigrations

# cd Users\MyPC\AppData\Local\Programs\Python\nanaapp
# python manage.py runserver
# http://127.0.0.1:8000/


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nanaapp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
