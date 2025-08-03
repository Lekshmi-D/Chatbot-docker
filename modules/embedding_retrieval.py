import os
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# In-memory vectorstore
model = SentenceTransformer('all-MiniLM-L6-v2')
VECTOR_DIM = model.get_sentence_embedding_dimension()  # Dynamically set dimension
index = None
stored_chunks = []


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def add_documents_to_vectorstore(docs: List[Dict]):
    global index, stored_chunks
    all_chunks = []
    for doc in docs:
        chunks = chunk_text(doc['content'])
        for chunk in chunks:
            all_chunks.append({'text': chunk, 'source': doc['filename']})
    if not all_chunks:
        return
    embeddings = model.encode([c['text'] for c in all_chunks])
    if index is None:
        index = faiss.IndexFlatL2(VECTOR_DIM)
        stored_chunks = []
    index.add(np.array(embeddings, dtype=np.float32))
    stored_chunks.extend(all_chunks)

def retrieve_relevant_chunks(query, top_k=5):
    global index, stored_chunks
    if index is None or not stored_chunks:
        return []
    query_emb = model.encode([query])
    D, I = index.search(np.array(query_emb, dtype=np.float32), top_k)
    return [stored_chunks[i] for i in I[0] if i < len(stored_chunks)]

def clear_vectorstore():
    global index, stored_chunks
    index = None
    stored_chunks = [] 