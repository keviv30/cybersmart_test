# TODO Application

## Overview
This TODO application is a full-stack web application developed using Django REST Framework for the backend and HTML, 
CSS, and vanilla JavaScript for the frontend. 
It allows users to create, view, update, and delete tasks with an additional feature of selecting a location for each task.
At the moment update and delete functions for the tasks are not implemented due to time constraint, but the backed is
available.
Based on the chosen location, the app displays the current weather and alters the task's background color accordingly.

I haven't implemented user authentication, due to time constraint. Please see the note further improvement section
for more detail.

## Features
- CRUD operations for tasks.
- Location-based task management with weather integration.
- Dynamic UI changes based on weather conditions.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x
- Poetry 
- Docker and Docker Compose (for containerization)

## Installation and Setup

### Requirements

- Python 3.11 or above
- Django 3.x
- SQLite database
- mypy
- black
- isort
- pytest-django

### Backend Setup
1. **Clone the Repository**
```
git clone repo_url
```

2. **Set Up a poetry**

Before you begin, make sure you have the following dependencies installed:

Poetry

Install poetry, which manages the python pakages 
https://python-poetry.org/docs/

1) Install poetry

```commandline
curl -sSL https://install.python-poetry.org | python3 -
```


3. **Install Dependencies**
```
cd cybersmart_test/
poetry install
```

4. **Environment Variables**

Set up the necessary environment variables or add them to a `.env` file in the cybersmart_test folder:

It uses openweathermap.org api key for the getting the weather data

```
SECRET_KEY='your_django_secret_key'
WEATHER_API_KEY='api-key'
```

5. **Run Migrations**
```
poetry run python manage.py migrate

```

6. **Add loction data**
```commandline
poetry run python manage.py populate_data
```

7. **Start the Backend Server**
```
poetry run python manage.py runserver
```

#### Testing

```commandline
poetry run pytest -sv
```

### Frontend Setup
1. **Navigate to Frontend Directory**
```
cd cybersmart_test/frontend
```

2. **Start a Simple HTTP Server**
Using Python:
```
python -m http.server 8000
```

### Docker Deployment

1) Build the docker image using docker-compose

```commandline
docker-compose build
```

2) Make migrations using docker compose

```commandline
docker-compose run app poetry run python manage.py migrate
```

3) Add location data

```commandline
docker-compose run app poetry run python manage.py populate_data
```

4) Run the server using docker-compose

```commandline
docker-compose up
```

5) Access the API at http://localhost:8080/tasks/

## Usage
After starting the backend and frontend servers, navigate to `http://localhost:8000` in your browser to access the 
TODO application.

1. **Create Task**: Click on the 'Create Task' button to open the task form. Fill in the details and select a location.
2. **Viewing Tasks**: View the list of tasks on the main page, each displayed with colors according to the current weather 
of their location.

#### Testing 

```commandline
docker-compose run app poetry run pytest -sv
```

## API Endpoints
- `/tasks/` - GET and POST tasks.
- `/tasks/<id>/` - GET, PATCH, and DELETE a specific task.
- `/locations/` - GET locations.
- `/weather/<str:location_name>/` - GET weather data for a location.

## Development Notes
- The application uses CORS headers; adjust the settings in `settings.py` as per your development 
or production environment.
- Make sure to update the frontend AJAX URLs to match the backend server address.


#### Further Improvements

Due to time constraints in the Django TODO list challenge, I prioritized core tasks like task management and weather 
data integration, and did not implement user authentication. 
This decision was strategic, focusing on demonstrating key backend skills within the limited timeframe. 
However, I acknowledge the importance of user authentication for security and user experience. 
If I had more time, I would have incorporated a comprehensive authentication system. 
I'm eager to showcase my full capabilities, including user authentication, in future projects.

We can add the following improvements to the project:

- Add User model to Tasks and add authentication
- Add more tests for the views and the utils.
- Provide more validation for the task requests.
- Production deployment using docker-compose and Github action.
- Configure docker-compose.prod.yml file for production deployment.
- Move frontend outside the backend directory
