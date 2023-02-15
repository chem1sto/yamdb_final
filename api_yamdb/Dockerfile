FROM python:3.7-slim
WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc && apt-get install nano
COPY api_yamdb/ .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
