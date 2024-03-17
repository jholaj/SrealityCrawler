FROM python:latest

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY . .