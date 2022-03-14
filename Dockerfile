#syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /app

COPY . .

CMD ["python", "main.py"]