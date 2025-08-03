# Contributing to Document QA Chatbot (llama.cpp)

This project is a modular Streamlit app for document-based QA using local LLMs via llama.cpp (GGUF models).

## Default/Tested Model

- **Model:** [Mistral-7B-Instruct-v0.2 Q4_K_M GGUF (TheBloke)](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf)
- **Download command:**
  ```bash
  wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O models/model.gguf
  ```
- Place the file in the `models/` directory as `model.gguf`.

## Project Structure

- `app.py` — Main Streamlit app, admin controls, and chat interface
- `modules/file_upload.py` — File upload and parsing (.txt, .pdf, .pptx)
- `modules/embedding_retrieval.py` — Embedding, chunking, and FAISS-based retrieval
- `modules/llm.py` — LLM interface using llama-cpp-python (GGUF models)
- `modules/chat_ui.py` — Chat UI logic (multi-turn, OpenAI-style)
- `requirements.txt` — Python dependencies
- `models/` — Directory for GGUF models

## Setup (Linux)

1. Clone the repo and enter the directory:
   ```bash
   git clone <repo-url>
   cd chatbot
   ```
2. Run the setup script:
   ```bash
   bash setup.sh
   ```
3. Download the default/tested GGUF model (see above) and place it in `models/model.gguf`.
4. Start the app:
   ```bash
   streamlit run app.py
   ```

## Coding Guidelines
- Use modular, readable code (see existing modules for style)
- Use `st.session_state` for all persistent UI state
- Use `llama-cpp-python` for LLM calls (no OpenAI API)
- All new features should be documented in the README and/or CONTRIBUTING.md
- Test your changes before submitting a PR

## Workflow
- Fork the repo and create a feature branch
- Make your changes and add/modify tests if needed
- Submit a pull request with a clear description
- Respond to code review feedback

## Contact
For questions, open an issue or contact the maintainers. 