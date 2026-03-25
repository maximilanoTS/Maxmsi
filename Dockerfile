# Dockerfile for Malware Detection Application

FROM python:3.11-slim

# Install ClamAV
RUN apt-get update && \
    apt-get install -y clamav clamav-daemon && \
    freshclam

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "your_application.py"]