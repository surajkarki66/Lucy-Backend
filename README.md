# Lucy: A NLP Powered Chatbot

Back-end code for a NLP Powered Chatbot (3rd year project) written in Python using FastAPI framework. It provides an handful of API endpoints to perform all the tasks related to chatbot.

---


## Table of Contents

1. [Installation](#1-installation)
2. [API endpoints](#2-api-endpoints)

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
DATABASE_USERNAME=<write username>
DATABASE_PASSWORD=<write password>
DATABASE_NAME=<write DB-name>
PGADMIN_EMAIL="admin@admin.com"
PGADMIN_PASSWORD="admin"
JWT_EXPIRE_SECONDS=604800
SECRET_KEY=<write security-key>
ALGORITHM="HS256"
HOST="0.0.0.0"
PORT=8080
DEVICE="cpu"
MODEL_NAME=<type of pretrained model which is either bert or distilbert>

```
5. Create a directory with name `lucy_models` in a root directory
6. Download the [pretrained_model](https://github.com/surajkarki66/Lucy-APIs/releases/tag/Lucy0.0.1) which is a file with `.pth` extension. There are two models one is a bert and another distil bert, you can choose any one of them. Based on the model you have to change the value MODEL_NAME environment variable to `bert` or `distilbert`.
7. Install all the dependencies
```bash
pip install -r "requirements.txt"
```
8. Migrate the database
```bash
alembic upgrade head
```
9. Migrate the data
```bash
python seeder.py
```
10. Run
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
DATABASE_NAME=<write DB-name>
PGADMIN_EMAIL="admin@admin.com"
PGADMIN_PASSWORD="admin"
JWT_EXPIRE_SECONDS=604800
SECRET_KEY=<write security-key>
ALGORITHM="HS256"
HOST="0.0.0.0"
PORT=8080
DEVICE="cpu"
MODEL_NAME=<type of pretrained model which is either bert or distilbert>

```
4. Create a directory with name `lucy_models` in a root directory
5. Download the [pretrained_model](https://github.com/surajkarki66/Lucy-APIs/releases/tag/Lucy0.0.1) which is a file with `.pth` extension. There are two models one is a bert and another distil bert, you can choose any one of them. Based on the model you have to change the value MODEL_NAME environment variable to `bert` or `distilbert`.
6. Run
    ```bash
    docker compose up
    ```
### 2. API Endpoints
You can access the documentation of the API by going to this link [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs) after running the backend server.
