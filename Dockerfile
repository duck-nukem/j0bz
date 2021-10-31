FROM python:3.10-slim-buster AS build
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /opt/app
COPY . /opt/app
RUN pip install -r /opt/app/requirements.txt

FROM gcr.io/distroless/python3
ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages

# Enable this to allow PyCharm to generate skeletons properly
COPY --from=build /bin/ /bin/

# application and its dependencies
COPY --from=build $PYTHONPATH $PYTHONPATH
COPY --from=build /opt/app/ /opt/app/

WORKDIR /opt/app

# Overwriting the default python entrypoint for better integration with tools (like IDEs)
ENTRYPOINT []
