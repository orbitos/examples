FROM python:3.10-alpine AS base
WORKDIR /app

RUN apk update && apk add gcc libc-dev linux-headers libffi-dev

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev
COPY . /app
ENV PYTHONUNBUFFERED=1