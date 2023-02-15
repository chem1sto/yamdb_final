FROM python:3.7-slim
WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY api_yamdb/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY api_yamdb/ .
COPY infra/.env .
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
