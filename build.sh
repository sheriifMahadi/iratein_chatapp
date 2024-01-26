#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
python manage.py migrate

# python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsu
docker run --rm -p 6379:6379 redis:7
