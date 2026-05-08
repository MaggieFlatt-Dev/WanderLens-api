#!/bin/bash

rm -rf WanderLensapi/migrations
rm db.sqlite3
python3 manage.py makemigrations WanderLensapi
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata categories
python3 manage.py loaddata triptypes
python3 manage.py loaddata trips
python3 manage.py loaddata stops

