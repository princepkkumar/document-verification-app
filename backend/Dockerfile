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

# --- NEW LINE ---
# Add the directory where pip installs command-line tools to the PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy the rest of the application source code
COPY ./src ./src

# Expose the port Render expects
EXPOSE 10000