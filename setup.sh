#!/bin/bash
set -e

# Create and activate virtual environment
echo "[1/5] Creating Python virtual environment..."
python3 -m venv chatbot-venv
source chatbot-venv/bin/activate

# Upgrade pip and install requirements
echo "[2/5] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create models directory
echo "[3/5] Creating models directory..."
mkdir -p models

# Download default/tested model (optional, prompt user)
echo "[4/5] Downloading default/tested GGUF model (Mistral-7B-Instruct-v0.2 Q4_K_M) ..."
echo "If you want to download it now, run:"
echo "  wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O models/model.gguf"
echo "Or download manually from: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF"

# Print next steps
echo "[5/5] Setup complete!"
echo "To start the app:"
echo "  source chatbot-venv/bin/activate"
echo "  streamlit run app.py" 