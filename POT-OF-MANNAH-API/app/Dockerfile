# Use the official Python 3.11 Alpine image as the base image
FROM python:3.11-alpine

# Set environment variables to ensure Python output is sent straight to the terminal (i.e., stdout)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install SQLite3 and other dependencies
RUN apk update && \
    apk add --no-cache sqlite sqlite-dev

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt using pip3
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
