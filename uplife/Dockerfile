# base image  
FROM python:3.10.3-buster


# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1


# update docker-image packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean


# Section 4- Project libraries and User Creation

# update pip 
RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

# install psycopg for connect to pgsql
RUN pip install --no-cache-dir psycopg2-binary

RUN pip install --no-cache-dir -r /tmp/requirements.txt \  
    && rm -rf /tmp/requirements.txt \  
    && useradd -U phototom_user \  
    && install -d -m 0755 -o phototom_user -g phototom_user /phototom-api/static

# Section 5- Code and User Setup
WORKDIR /phototom-api

USER phototom_user:phototom_user

COPY --chown=phototom_user:phototom_user . .


EXPOSE 8000
CMD ["gunicorn","--bind", ":8000", "--workers", "3", "core.wsgi:application"]