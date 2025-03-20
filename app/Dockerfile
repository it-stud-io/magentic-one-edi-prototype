# Use the official Python image from the DockerHub
FROM python:3.13.2-slim-bookworm

# Update the package list & install git
RUN apt-get update
RUN apt-get install -y git

# Upgrade pip & install uv
RUN pip install --upgrade pip
RUN pip install uv

# Set the working directory in docker
WORKDIR /app

# Setup AutoGen and MagenticOne
RUN git clone https://github.com/microsoft/autogen.git --branch python-v0.4.8.2
WORKDIR /app/autogen/python
RUN uv sync --all-extras
RUN . .venv/bin/activate

#WORKDIR /app/autogenpackages/autogen-magentic-one
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml .

# Install any dependencies
RUN pip install .

# Copy the content of the local src directory to the working directory
COPY . .

# Install playwright
RUN playwright install
RUN playwright install-deps

RUN chmod +x run.sh

# Specify the command to run on container start
CMD ["./run.sh"]