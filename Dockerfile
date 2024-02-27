FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000