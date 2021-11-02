FROM python:3.10-slim-buster AS build
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y \
        libpython3.7 \
        libpq-dev \
        gcc
RUN pip install --upgrade pip

WORKDIR /opt/app
COPY . /opt/app
RUN pip install -r /opt/app/requirements.txt

# Overwriting the default python entrypoint for better integration with tools (like IDEs)
ENTRYPOINT []
