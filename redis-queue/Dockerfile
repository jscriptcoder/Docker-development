FROM python:3.9-slim

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt

COPY . .
CMD rq worker myapp-queue --url ${REDIS_URL}