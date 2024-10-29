#!/bin/bash
python manage.py collectstatic --noinput
gunicorn --workers 2 -b 0.0.0.0:8000 ai_project.wsgi:application
