# Step 1: Use official Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    wget \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the repo into /app
RUN git clone https://github.com/Lekshmi-D/Chatbot-docker.git

# Step 5: Install Python dependencies
RUN pip install -r Chatbot-docker/requirements.txt