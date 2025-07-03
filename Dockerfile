# Use official Python image
FROM python:3.12-slim

ARG DATABASE_URL
ENV DATABASE_URL=$DATABASE_URL

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project code
COPY event_app/ event_app/
COPY static/ static/
COPY templates/ templates/
COPY user_app/ user_app/
COPY woofspot_project/ woofspot_project/
COPY manage.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files (optional for production)
RUN python manage.py collectstatic --noinput

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port (optional)
EXPOSE 8001

# Start server
CMD ["gunicorn", "woofspot_project.wsgi:application", "--bind", "0.0.0.0:8001"]
