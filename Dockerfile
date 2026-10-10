FROM python:3.12-slim

WORKDIR /app

COPY application/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY application/app ./app

EXPOSE 5000

CMD ["python", "app/app.py"]
