FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
