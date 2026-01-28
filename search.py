from sentence_transformers import SentenceTransformer
import os
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

DATA_DIR = "data/sample_docs"

documents = []
doc_names = []

# Read documents
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)
            doc_names.append(filename)

# Create embeddings for documents
doc_embeddings = model.encode(documents)

# User query
query = input("Enter your search query: ")

# Convert query to embedding
query_embedding = model.encode([query])[0]

# Cosine similarity function
def cosine_similarity(a, b):
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    return np.dot(a, b)

# Calculate similarity scores between query and each document
similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

# Find the index of the best matching document
best_idx = np.argmax(similarities)

print(f"\nBest matching document: {doc_names[best_idx]}")
print(f"Similarity score: {similarities[best_idx]:.4f}")
print(f"Content:\n{documents[best_idx]}")
