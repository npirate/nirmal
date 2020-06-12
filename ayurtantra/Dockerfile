# Pull base image
FROM python:3.7

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /code

# Install dependencies
# COPY Pipfile Pipfile.lock /code/
#RUN cd /code/ && pip install pipenv && pipenv install --system
RUN pip install django==2.2 && pip install django-crispy-forms && pip install gunicorn

# Copy project
COPY . /code/