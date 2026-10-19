# syntax=docker/dockerfile:1
FROM python:3.12-slim

# --- Environment ---
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# --- Working directory ---
WORKDIR /app

# --- System dependencies (as root) ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Non-root user with fixed UID/GID ---
ARG USER_ID=1001
ARG GROUP_ID=1001
RUN groupadd --gid $GROUP_ID appuser \
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home --shell /bin/bash appuser \
    && chown appuser:appuser /app

# --- Copy project code with correct ownership ---
COPY --chown=appuser:appuser event_app/ event_app/
COPY --chown=appuser:appuser static/ static/
COPY --chown=appuser:appuser templates/ templates/
COPY --chown=appuser:appuser user_app/ user_app/
COPY --chown=appuser:appuser woofspot_project/ woofspot_project/
COPY --chown=appuser:appuser manage.py .
COPY --chown=appuser:appuser requirements.txt .

# --- Install Python deps as root (go to /usr/local, readable by all users) ---
RUN pip install --no-cache-dir -r requirements.txt

# --- Switch to non-root for everything else ---
USER appuser

# --- Collect static with SQLite dummy (DB not needed at build time) ---
RUN DATABASE_URL="sqlite:////tmp/dummy.sqlite3" \
    python manage.py collectstatic --noinput \
    && rm -f /tmp/dummy.sqlite3

# --- Expose ---
EXPOSE 8001

# --- Start server (port 8001 > 1024, no root needed) ---
CMD ["gunicorn", "woofspot_project.wsgi:application", "--bind", "0.0.0.0:8001"]
