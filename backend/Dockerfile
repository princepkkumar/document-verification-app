# backend/Dockerfile

# Start from a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY ./src ./src

# Copy the new entrypoint script into the container
COPY ./entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x ./entrypoint.sh

# Set the entrypoint script as the command to run when the container starts
ENTRYPOINT ["./entrypoint.sh"]