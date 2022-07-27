FROM python:3
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
COPY Pipfile .
COPY Pipfile.lock .
COPY . /usr/src/app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install -r requirements.txt
COPY . .
