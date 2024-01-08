# Lucy: A NLP Powered Chatbot

This is an end-to-end implementation of deep learning. The Lucy is a web-based chatbot, which gives you information about Nepal Engineering College from where I graduated and this was my second minor college project. This repository contains back-end code for a NLP Powered Chatbot (3rd year project) written in Python using FastAPI framework. It provides a handful of API endpoints to perform all the tasks related to the chatbot.

---

## Table of Contents

- [Lucy: A NLP Powered Chatbot](#lucy-a-nlp-powered-chatbot)
  - [Table of Contents](#table-of-contents)
    - [1. Installation](#1-installation)
      - [i. Locally](#i-locally)
      - [ii. Using Docker](#ii-using-docker)
    - [2. API Endpoints](#2-api-endpoints)
    - [3. Running Frontend](#3-running-frontend)

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
   DATABASE_USERNAME="postgres"
   DATABASE_PASSWORD="postgres"
   DATABASE_NAME="lucy"
   PGADMIN_EMAIL="admin@admin.com"
   PGADMIN_PASSWORD="admin"
   JWT_EXPIRE_SECONDS=604800
   SECRET_KEY="m!-WBkY461NKLG3RYOZfds"
   ALGORITHM="HS256"
   HOST="0.0.0.0"
   PORT=8080
   DEVICE="cpu"
   MODEL_NAME="bert"

   ```
5. [Click here](https://github.com/surajkarki66/Lucy-Backend/releases/download/Lucy0.0.1/lucy_bert.pth) and download the pre-trained `lucy_bert.pth` file and paste it inside the `lucy_models` directory of project root.
6. Install all the dependencies
   ```bash
   pip install -r "requirements.txt"
   ```
7. Migrate the database
   ```bash
   alembic upgrade head
   ```
8. Migrate the data
   ```bash
   python seeder.py
   ```
9. Run
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
   DATABASE_USERNAME="lucyuser"
   DATABASE_PASSWORD="lucypassword"
   DATABASE_NAME="lucy"
   PGADMIN_EMAIL="admin@admin.com"
   PGADMIN_PASSWORD="admin"
   JWT_EXPIRE_SECONDS=604800
   SECRET_KEY="m!-WBkY461NKLG3RYOZf"
   ALGORITHM="HS256"
   HOST="0.0.0.0"
   PORT=8080
   DEVICE="cpu"
   MODEL_NAME="bert"

   ```

4. [Click here](https://github.com/surajkarki66/Lucy-Backend/releases/download/Lucy0.0.1/lucy_bert.pth) and download the pre-trained `lucy_bert.pth` file and paste it inside the `lucy_models` directory of project root.
5. Run
   ```bash
   docker compose up
   ```

### 2. API Endpoints

You can access the documentation of the API by going to this link [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs) after running the backend server.

### 3. Running Frontend

To run the frontend of the Lucy first go to this [link](https://github.com/surajkarki66/Lucy-Frontend) and follow the instructions.
