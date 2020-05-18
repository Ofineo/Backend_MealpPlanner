FROM python:3.8.2-slim

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DATABASE_URL="postgres://0.0.0.0:5432/meals"


ENTRYPOINT ["gunicorn", "-b", ":8080", "app:APP"]