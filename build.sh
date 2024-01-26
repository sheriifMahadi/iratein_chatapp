#!/usr/bin/env bash
# exit on error
set -o errexit

source /iratein_env/bin/activate
cd /code


# python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createsu

python manage.py runserver 0.0.0.0:8000
docker run -p 6379:6379 -d redis:5
docker container ls