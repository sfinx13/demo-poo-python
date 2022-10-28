#syntax=docker/dockerfile:1

FROM python:3.12.0a1-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]