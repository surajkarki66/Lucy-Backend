# Lucy: A NLP Powered Chatbot

Back-end code for a NLP Powered Chatbot (3rd year project) written in Python using FastAPI framework. It provides an handful of API endpoints to perform all the tasks related to chatbot.

---

## Table of Contents

1. [Installation](#1-installation)
2. [API endpoints](#2-api-endpoints)
3. [Running Frontend](#3-running-frontend)

---

### 1. Installation

#### i. Locally

1. Install [postgresql](https://www.postgresql.org/download/)
2. Create a database with name `lucy`
   ```bash
   sudo -iu postgres
   createdb -h localhost -p 5432 -U postgres lucy
   ```
3. Clone this repo
4. Create an .env file in a project root directory and add the following information

   ```
   ENV_STATE="development"
   API_NAME="Lucy-API"
   API_DESCRIPTION="These are the restful API's which is used to talk with Lucy. The ultimate goal of this project is to provide a common, user-friendly, efficient way to retrieve the response to a query asked by end-users."
   API_VERSION="0.0.2"
   DATABASE_HOSTNAME="localhost"
   DATABASE_PORT=5432
   DATABASE_USERNAME=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_NAME="lucy"
   PGADMIN_EMAIL="admin@admin.com"
   PGADMIN_PASSWORD="admin"
   JWT_EXPIRE_SECONDS=604800
   SECRET_KEY=<write strong security-key>
   ALGORITHM="HS256"
   HOST="0.0.0.0"
   PORT=8080
   DEVICE="cpu"
   MODEL_NAME="distilbert"

   ```

5. Install all the dependencies
   ```bash
   pip install -r "requirements.txt"
   ```
6. Migrate the database
   ```bash
   alembic upgrade head
   ```
7. Migrate the data
   ```bash
   python seeder.py
   ```
8. Run
   ```bash
   python manage.py
   ```

#### ii. Using Docker

1. Clone the repo
2. Install [docker](https://docs.docker.com/get-docker/)
3. Create an .env file in a project root directory and add the following information

   ```
   ENV_STATE="development"
   API_NAME="Lucy-API"
   API_DESCRIPTION="These are the restful API's which is used to talk with Lucy. The ultimate goal of this project is to provide a common, user-friendly, efficient way to retrieve the response to a query asked by end-users."
   API_VERSION="0.0.2"
   DATABASE_HOSTNAME="postgres"
   DATABASE_PORT=5432
   DATABASE_USERNAME=<write a db username>
   DATABASE_PASSWORD=<write a db password>
   DATABASE_NAME="lucy"
   PGADMIN_EMAIL="admin@admin.com"
   PGADMIN_PASSWORD="admin"
   JWT_EXPIRE_SECONDS=604800
   SECRET_KEY=<write security-key>
   ALGORITHM="HS256"
   HOST="0.0.0.0"
   PORT=8080
   DEVICE="cpu"
   MODEL_NAME="distilbert"

   ```

4. Run
   ```bash
   docker compose up
   ```

### 2. API Endpoints

You can access the documentation of the API by going to this link [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs) after running the backend server.

### 3. Running Frontend

To run the frontend of the Lucy first go to this [link](https://github.com/surajkarki66/Lucy-Frontend) and follow the instructions.
