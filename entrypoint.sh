#!/bin/sh

# Run database migrations
python3 manage.py migrate --noinput

# Start the Django development server
python3 manage.py runserver 0.0.0.0:8000

