# UpLife

College project aimed at making the donation of blood and medicine easier and more manageable locally.

#

## Requirements

- Python 3.9+

All other dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

#

## Installation

- Clone or [download](https://github.com/Iah-Uch/uplife-api/archive/refs/heads/main.zip) this repository;

- Change to the project's directory;

  - On `\uplife-api`
    - `cd uplife`

- Setup Environment Variables;

  - On `/uplife-api/uplife`

    - Import or create a **.env** file

      - Variables needed for **this project**:

        - **SECRET_KEY**=< Django generated secret key ([not the default](https://humberto.io/blog/tldr-generate-django-secret-key/)) >

          **ALLOWED_HOSTS**=< allowed hosts IP's and/or domain name >

          **CSRF_TRUSTED_ORIGINS**=< Trusted request origins full URL or IP >

          **DEBUG**=True (remove this one for production mode)

        - _DATABASE_URL=< **Optional** database url to use a specific database (default is SQLite3) >_

    - Consider using [this package to handle .env files on git](https://github.com/harrisonpim/dotenv-stripout)

- <details closed="true"><summary><h4>Virtual Env</h4></summary>
    - Create a virtual environment;

      - On `/uplife-api/uplife`
        - `python -m venv venv`
        - Activate the venv
          - `.\venv\Scripts\activate`

  - Install the dependencies;

    - On `/uplife-api/uplife`
      - `pip install -r .\requirements.txt`

  - Run initial management commands

    - On `/uplife-api/uplife`
      - Create the database Migrations
        - `python .\manage.py makemigrations`
      - Run the Migrations
        - `python .\manage.py migrate`
      - Collect Static Files
        - `python .\manage.py collectstatic --noinput`

  - Create a Super User for testing

    - On `/uplife-api/uplife`
      - ` python .\manage.py createsuperuser`

  - Run the project - On `/uplife-api/uplife` - ` python .\manage.py runserver`
  </details>

- <details closed="true">
  <summary> 
    <h4>Docker</h4> 
  </summary>

  - Setup Environment Variables Caveat;

    - Inside DockerFile there are several attributes to change before deploying, but it is fine as is for testing

  - Run Docker Compose Routine;

    - On `\uplife-api\uplife` - `docker compose up --build`
  </details>

#

## OAS3 Docs Options
- Go to `<host>:<port>/api/docs/`
- Access the static schema on [SwaggerHub](https://app.swaggerhub.com/apis-docs/Iah-Uch/uplife-api/0.0.1)

#

## Stack
- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
: Python is a popular and powerful programming language widely used for web development, data analysis, artificial intelligence, and more.
- ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white)
: Django is a high-level Python web framework designed for rapid development and clean, pragmatic design.
- ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
: A powerful, open-source relational database system.
- ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
: A containerization platform that allows developers to easily package applications and their dependencies into portable containers.

#

## Libraries Used
- **djangorestframework**: Django REST framework is a powerful and flexible toolkit for building Web APIs.

- **gunicorn**: Gunicorn is a Python WSGI HTTP Server for UNIX. It allows you to run your Django application as a standalone server.

- **psycopg2-binary**: psycopg2-binary is a PostgreSQL adapter for Python. It provides efficient access to PostgreSQL databases.

- **whitenoise**: whitenoise allows you to serve static files efficiently from your Django application. It provides a simple API to serve static files directly from your project's root directory.

- **django-rest-knox**: django-rest-knox is an authentication library for Django REST Framework. It provides a secure way to authenticate users through tokens.

- **drf-spectacular**: drf-spectacular is an OpenAPI 3 schema generator for Django REST framework. It simplifies the generation of API documentation by providing a straightforward API to generate OpenAPI 3 schema.

- **dj-database-url**: This library allows the Django application to utilize the DATABASE_URL environment variable for easy configuration of database connection settings.

- **django-cleanup**: django-cleanup is a simple Django app for cleaning up files that are no longer needed. 

- **django-cors-headers**: This library provides a middleware that allows Cross-Origin Resource Sharing (CORS) in Django applications. It allows cross-domain requests from web browsers to any server.

- **django-currentuser**: This library provides a way to get the currently logged-in user anywhere in your code. It allows you to get the user object without passing it around in function calls.

- **django-environ**: This library allows you to store configuration in environment variables. This makes it easy to configure your Django application without hardcoding any settings.

- **django-localflavor**: django-localflavor is a collection of assorted pieces of code that are useful for particular countries or cultures. It provides country-specific Django helpers, form fields, and widgets.


