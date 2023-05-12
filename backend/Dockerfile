FROM python:3.11-slim

# Setup environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install Python dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system --deploy

# Prepare environment
WORKDIR /app/backend
COPY . /app/backend

# Create a non-root user and add permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" docker && chown -R docker:docker /app
USER docker

# Run the application
ENTRYPOINT ["bash", "entrypoint.sh"]
EXPOSE 8000
