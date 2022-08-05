FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/src/source

COPY showroom /usr/src/source
COPY requirements.txt /usr/src/source
COPY env/ /usr/src/source
COPY Dockerfile /usr/src/source
COPY docker-compose.yml /usr/src/source

RUN pip install -r requirements.txt