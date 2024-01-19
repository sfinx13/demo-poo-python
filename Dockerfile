#syntax=docker/dockerfile:1

FROM python:3.13.0a3-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]