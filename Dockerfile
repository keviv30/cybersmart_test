# Use the official Python base image
FROM python:3.11.6-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY poetry.lock pyproject.toml ./

RUN pip install poetry

# Install the Python dependencies
RUN poetry install

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080
