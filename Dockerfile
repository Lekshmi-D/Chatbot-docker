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

# Step 4: Copy your local code into container
COPY . .

# Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Download the GGUF model into models/ folder
RUN mkdir -p models && \
    wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf \
    -O models/model.gguf

# Step 7: Expose Streamlit port
EXPOSE 8501

# Step 8: Run the app
CMD ["streamlit", "run", "app.py"]