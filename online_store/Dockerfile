FROM python:3.9.10
WORKDIR /app
RUN pip install gunicorn==20.1.0
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "online_store.wsgi"]