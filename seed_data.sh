#!/bin/bash

rm db.sqlite3
rm -rf ./WanderLensapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations WanderLensapi
python3 manage.py migrate WanderLensapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata categories
python3 manage.py loaddata triptypes

