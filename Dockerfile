FROM python:3.11

RUN apt update -y && apt upgrade -y
RUN apt install -y make

WORKDIR /app

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN pip install poetry
RUN poetry install --no-dev --no-root

COPY app app
COPY resources resources
COPY gunicorn.conf.py gunicorn.conf.py

ENV PYTHONPATH=/app \
    MODEL_PARAMETER_DIR=/app/resources/model_params

CMD poetry run gunicorn app.main:app