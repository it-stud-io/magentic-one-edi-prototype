# Use the official Python image from the DockerHub
FROM python:3.13.2-slim-bookworm

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory in docker
WORKDIR /api

# Copy the dependencies file to the working directory
COPY pyproject.toml .

# Install any dependencies
RUN pip install .

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "api.py"]