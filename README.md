# WanderLens API

The back end for WanderLens, a travel tracking app where users can log trips and the stops they made along the way.

Built with Django REST Framework and SQLite.

## Features

- User authentication (register, login)
- Full CRUD for trips and stops
- Categorize stops and assign trip types
- Stops include location data (lat/long, city, country) and a visited date

## Tech Stack

- Python 3.10
- Django
- Django REST Framework
- SQLite

## Getting Started

```bash
pipenv install
pipenv shell
sh seed_data.sh
python manage.py runserver
```

The API will be running at `http://localhost:8000`.

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/register` | Create a new user |
| POST | `/login` | Log in |
| GET | `/current_user` | Get logged in user |
| GET/POST | `/api/trips` | List or create trips |
| GET/PUT/DELETE | `/api/trips/:id` | Get, update, or delete a trip |
| GET/POST | `/api/stops` | List or create stops |
| GET/PUT/DELETE | `/api/stops/:id` | Get, update, or delete a stop |
| GET | `/api/triptypes` | List trip types |
| GET | `/api/categories` | List categories |
