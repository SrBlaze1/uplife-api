# UpLife

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

## OAS3 Docs Options

- Go to `<host>:<port>/api/docs/`
