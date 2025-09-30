# backend/Dockerfile

FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This is the most important line
ENV PATH="/root/.local/bin:${PATH}"

COPY ./src ./src

EXPOSE 10000