from llama_cpp import Llama
import os

# Path to your GGUF model file (update as needed)

#this is the one I use
LLAMA_MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", "./models/model.gguf")

#LLAMA_MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", "models/phi-2.Q4_K_M.gguf")


# Singleton for the Llama model
_llama_instance = None

def get_llama_instance():
    global _llama_instance
    if _llama_instance is None:
        _llama_instance = Llama(model_path=LLAMA_MODEL_PATH, n_ctx=4096, n_threads=4)
    return _llama_instance

def get_llm_response(context, chat_history, user_input):
    llama = get_llama_instance()
    # Handle greetings interactively
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    if user_input.strip().lower() in greetings:
        return "Hello! 👋 How can I assist you with your documents today?"
    # If no context is found, return a funny but professional fallback
    if not context:
        return "Oops! My knowledge vault is empty on that one. 🕵️‍♂️ Try asking about something in the uploaded documents, or maybe bribe me with more files! 😉"
    # Build the prompt with context and chat history
    prompt = "You are a helpful assistant. Use the following context to answer the user's question. If its a random conversation, please feel free to answer politely and without the context. But if its something the user seriously wants to know, take care to only include information that can be found in our database.\n"
    for c in context:
        prompt += f"Source: {c['source']}\n{c['text']}\n\n"
    if chat_history:
        for turn in chat_history:
            prompt += f"User: {turn['user']}\nAssistant: {turn['bot']}\n"
    prompt += f"User: {user_input}\nAssistant:"
    # Generate response
    output = llama(prompt, max_tokens=512, stop=["User:", "Assistant:"])
    response = output["choices"][0]["text"].strip()
    # If the model gives a non-answer, fallback
    if not response or any(x in response.lower() for x in ["i don't know", "as an ai", "cannot answer", "no information"]):
        return "Sorry, the data is not available. But if you upload more documents, I might just become a genius! 🤓"
    return response 