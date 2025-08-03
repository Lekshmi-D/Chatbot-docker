import streamlit as st
from modules.embedding_retrieval import retrieve_relevant_chunks
from modules.llm import get_llm_response

def chat_interface():
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    st.title("Chat with your documents")
    # Display chat history in a chat-like format
    for turn in st.session_state['chat_history']:
        with st.chat_message("user"):
            st.markdown(turn["user"])
        with st.chat_message("assistant"):
            st.markdown(turn["bot"])
    # Chat input at the bottom
    user_input = st.chat_input("Type your message and press Enter...")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        # Retrieve context
        context = retrieve_relevant_chunks(user_input)
        if not context:
            st.warning("No documents indexed. Please ask the admin to upload documents.")
            return
        chat_history = st.session_state['chat_history']
        with st.spinner("Assistant is typing..."):
            try:
                response = get_llm_response(context, chat_history, user_input)
            except Exception as e:
                st.error(f"LLM error: {e}")
                return
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state['chat_history'].append({"user": user_input, "bot": response}) 