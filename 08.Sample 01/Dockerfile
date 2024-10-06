# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the 'web' folder to /app
COPY web /app

# Install Flask in the container
RUN pip install --no-cache-dir Flask

# Expose port 5000 for the Flask app
EXPOSE 5123

# Command to run the Flask app
CMD ["python", "random_numbers_api.py"]
