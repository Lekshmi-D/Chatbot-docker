import streamlit as st
from modules.file_upload import handle_file_upload, clear_uploaded_files
from modules.embedding_retrieval import (add_documents_to_vectorstore, retrieve_relevant_chunks, clear_vectorstore)
from modules.llm import get_llm_response
from modules.chat_ui import chat_interface

# the name in tab
st.set_page_config(page_title="Document QA Chatbot", layout="wide")

# Admin section: Upload and manage documents
def admin_controls():
    # Add logo at the top of the sidebar
    st.sidebar.image("80342670.cms.avif", use_container_width=True)
    st.sidebar.header("Admin Controls")
    uploaded_files = st.sidebar.file_uploader(
        "Upload .txt, .pdf, .pptx files", type=["txt", "pdf", "pptx"], accept_multiple_files=True, key="file_uploader"
    )
    if uploaded_files:
        docs = handle_file_upload(uploaded_files)
        add_documents_to_vectorstore(docs)
        st.sidebar.success(f"Uploaded and indexed {len(docs)} documents.")
    if st.sidebar.button("Clear Uploaded Files & Vectorstore"):
        clear_uploaded_files()
        clear_vectorstore()
        st.sidebar.success("Cleared all uploaded files and vectorstore.")
    if st.sidebar.button("Reset Chat"):
        st.session_state.clear()
        st.sidebar.success("Chat history reset.")

# Main chat interface (user only sees this)
def main():
    st.title("Document QA Chatbot (llama.cpp)")
    st.info("Ask questions about the uploaded documents. (User mode: only QA, no upload)\nLLM runs locally using llama.cpp (GGUF model via llama-cpp-python).")
    chat_interface()

if __name__ == "__main__":
    admin_controls()
    main() 