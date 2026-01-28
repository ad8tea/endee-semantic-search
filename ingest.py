from sentence_transformers import SentenceTransformer
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Folder containing documents
DATA_DIR = "data/sample_docs"

documents = []
doc_names = []

# Read files
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)
            doc_names.append(filename)

# Convert documents to embeddings
embeddings = model.encode(documents)

print("Documents ingested:", doc_names)
print("Number of embeddings:", len(embeddings))
