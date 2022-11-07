FROM --platform=linux/amd64  python:3.10-slim-buster
RUN apt-get -y update && \
  apt-get install -y --no-install-recommends \
    python-dev \
    default-libmysqlclient-dev \
    default-mysql-client \
    git \
    make \
    bash \
    curl \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pipenv
RUN mkdir /app


# install python packages before copying entire source code
COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app/
RUN pipenv sync
