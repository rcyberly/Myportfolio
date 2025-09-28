# Use the official Python base image
FROM python:3.11-slim

# Set environment variables for the application
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the port Cloud Run will use
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
# We use separate steps for caching efficiency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project code into the container
COPY . /app

# Collect static files (This prepares the files for Firebase Hosting)
RUN python manage.py collectstatic --noinput

# Command to run the Django application using Gunicorn
# 'myproject.wsgi' is derived from your WSGI_APPLICATION setting.
CMD exec gunicorn --bind :${PORT} --workers 2 --threads 2 --timeout 60 myproject.wsgi