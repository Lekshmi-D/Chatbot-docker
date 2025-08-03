# Streamlit Document QA Chatbot (llama.cpp Edition)

This app allows an admin to upload `.txt`, `.pdf`, or `.pptx` documents. Users can then ask questions, and the chatbot will answer using the uploaded documents as context, powered by a locally hosted LLM (llama.cpp, GGUF model, via llama-cpp-python).

## Default/Tested Model

- **Model:** [Mistral-7B-Instruct-v0.2 Q4_K_M GGUF (TheBloke)](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf)
- **Download command:**
  ```bash
  wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O models/model.gguf
  ```
- Place the file in the `models/` directory as `model.gguf`.

## Features
- Admin uploads and indexes documents (no user upload)
- Supports `.txt`, `.pdf`, `.pptx` files
- Embedding and retrieval with FAISS and sentence-transformers
- Chatbot uses a local LLM via llama.cpp (GGUF model, e.g. Qwen, Llama2, Mistral, etc.)
- Modular codebase

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download the default/tested GGUF model:**
   ```bash
   wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O models/model.gguf
   ```

3. **Set the model path (optional):**
   By default, the app looks for `./models/model.gguf`. To use a different path, set the environment variable:
   ```bash
   export LLAMA_MODEL_PATH="/path/to/your/model.gguf"
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage
- **Admin:** Use the sidebar to upload documents and manage/reset the database and chat.
- **User:** Ask questions in the main chat window. The bot will answer using the uploaded documents.

## Notes
- All data is stored in memory (no persistent storage).
- Only the admin can upload documents; users can only ask questions.
- The LLM runs locally using llama.cpp via the `llama-cpp-python` library. 