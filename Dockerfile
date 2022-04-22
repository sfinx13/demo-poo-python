#syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]