# Document QA Chatbot Workflow Diagram

```mermaid
flowchart TD
    A[Admin uploads .txt/.pdf/.pptx] --> B[Parse & extract text]
    B --> C[Chunk & embed text (sentence-transformers)]
    C --> D[Store embeddings in FAISS index]
    E[User asks a question] --> F[Retrieve relevant chunks (FAISS)]
    F --> G[Build prompt with context & chat history]
    G --> H[llama-cpp-python (GGUF model) generates response]
    H --> I[Display response in chat UI]
    D -.-> F
```

**Legend:**
- Admin: Uploads and manages documents
- User: Asks questions in chat
- LLM: Local GGUF model via llama-cpp-python
- All state is in-memory (no persistent storage) 