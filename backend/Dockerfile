# backend/Dockerfile

# Start from a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including Tesseract and the missing graphics library for OpenCV
RUN apt-get update && apt-get install -y tesseract-ocr libgl1-mesa-glx

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY ./src ./src

# Expose the port Render expects
EXPOSE 10000

# The command to run the application when the container starts
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:app", "--bind", "0.0.0.0:10000"]