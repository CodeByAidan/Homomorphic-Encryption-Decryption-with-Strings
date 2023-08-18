# Build: docker build -t homomorphic-encryption-api .
# Run: docker run homomorphic-encryption-api:latest

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the api directory contents into the container at /app
COPY . /app/
COPY log /app/log
COPY startup.sh /app/startup.sh

# Install numpy
RUN pip install --no-cache-dir numpy

# Grant execution permission to the startup script
RUN chmod +x /app/startup.sh

# Run the startup script as the primary command
CMD ["/app/startup.sh"]
