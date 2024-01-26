#!/usr/bin/env bash
# exit on error
set -o errexit


python manage.py collectstatic --no-input
python manage.py makemigrations chatapp
python manage.py makemigrations chatapp_api
python manage.py migrate
python manage.py createsu
