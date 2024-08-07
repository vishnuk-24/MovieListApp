# Movie List Application Backend

This is the backend for the Movie List Application, a FastAPI-based service that provides information about movies and people in the movie industry.

## Project Structure

```
.
├── api
│   ├── __init__.py
│   └── routes.py
├── auth.py
├── commands.txt
├── create_initial_users.py
├── database.py
├── import_datasets.py
├── main.py
├── models
│   ├── __init__.py
│   ├── movie.py
│   ├── person.py
│   └── user.py
├── movie_database.db
├── requirements.txt
└── schemas
    ├── __init__.py
    ├── movie.py
    ├── person.py
    └── user.py
```

- `api/`: Contains API route definitions
- `models/`: Defines database models
- `schemas/`: Defines Pydantic schemas for request/response validation
- `auth.py`: Handles authentication logic
- `database.py`: Sets up database connection
- `import_datasets.py`: Script to import initial datasets
- `create_initial_users.py`: Script to create initial users
- `main.py`: Main application file
- `requirements.txt`: List of project dependencies

## Initial Setup

Before running the application, you need to perform some initial setup steps:

1. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Import Datasets**:
   Run the `import_datasets.py` script to populate the database with initial movie and person data:
   ```
   python import_datasets.py
   ```
   This step is crucial as it sets up the core data for the application.

3. **Create Initial Users**:
   Run the `create_initial_users.py` script to set up some initial user accounts:
   ```
   python create_initial_users.py
   ```
   This step is important for testing authentication and user-specific features.

## Running the Application

To start the FastAPI server:

```
uvicorn main:app --reload
```

The server will start, and you can access the API at `http://localhost:8000`.

## API Documentation

Once the server is running, you can view the interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Authentication

The API uses JWT for authentication. To access protected endpoints:

1. Register a new user or use one of the initial users created.
2. Obtain a token by sending a POST request to `/token` with username and password.
3. Include the token in the `Authorization` header of subsequent requests.

## Main Features

- Search for movies with various filters
- Search for people in the movie industry
- User registration and authentication
