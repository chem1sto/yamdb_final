FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8001" ]
