## Project name
Late Show API challenge. This is a restful API for a late night tv show system that has been built using flask, postgresql and jwt authentication

## Project author
The project was developed by Lisa Alusa

## Features
- MVC Architecture
- PostgreSQL Database
- JWT-based Authentication
- Secure Routes
- Seeded Data
- Postman Collection for API Testing

## Setup Instructions
1. Clone the repository
git clone https://github.com/Alusa05/late-show-api-challenge
cd late-show-api-challenge

2. Install Dependencies
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell

3. PostgreSQL Setup
Create a database using psql or pgAdmin:
CREATE DATABASE late_show_db;

4. Configure Environment
Edit `server/config.py`:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
JWT_SECRET_KEY = "your-secret-key"

