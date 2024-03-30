FROM python:3.11-buster

ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt install -y python3-dev

RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

EXPOSE 8000

COPY . .