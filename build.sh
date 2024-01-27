#!/usr/bin/env bash
# exit on error
set -o errexit

source /iratein_env/bin/activate
cd /code


# python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsu
# python manage.py runworker channel_layer -v2

daphne -b -0.0.0.0 -p 8000 core.asgi:application 
docker run -p 6379:6379 -d redis:5


