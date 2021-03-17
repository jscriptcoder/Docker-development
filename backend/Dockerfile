FROM python:3.9-slim

WORKDIR /usr/app

RUN apt-get update

COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt

COPY . .
CMD gunicorn --workers 4 --threads 20 --bind 0.0.0.0:5000 --log-level info myapp.wsgi:app