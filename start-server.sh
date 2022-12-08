#!/usr/bin/env bash
python django_api/manage.py makemigrations
python django_api/manage.py migrate
python django_api/manage.py createcachetable

# no-input flag takes from env variables DJANGO_SUPERUSER_USERNAME/PASSWORD/EMAIL
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python django_api/manage.py createsuperuser --no-input
fi
(cd django_api; gunicorn django_api.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"

#python django_api/manage.py runserver 0.0.0.0:8000
