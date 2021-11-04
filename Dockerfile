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

EXPOSE 80
CMD ["./bin/run_webserver.sh"]
