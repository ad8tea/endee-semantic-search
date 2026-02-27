# Endee Semantic Search Demo
This project demonstrates a simple semantic search system built using transformer embeddings and inspired by vector database principles used in Endee.

It converts text documents into vector embeddings and retrieves the most relevant result (Top-1) based on semantic similarity.

---

## Overview

Traditional keyword search matches exact words.
Semantic search understands meaning.

This project:

Converts documents into embeddings using a transformer model

Stores embeddings as vectors

Computes cosine similarity

Returns the most relevant document (Top-1)

---

## Tech Stack
1. Python
2. sentence-transformers
3. NumPy
4. Transformer Model: all-MiniLM-L6-v2
5. Similarity Metric: Cosine similarity

---

## Key Features

- Transformer-based embeddings using `all-MiniLM-L6-v2`
- Cosine similarity ranking
- Top-5 semantic retrieval
- Lightweight and efficient implementation
- Modular structure for future scaling (RAG-ready)

---

## System Architecture

1. Text documents are stored in `data/sample_docs/`
2. Documents are converted into vector embeddings using SentenceTransformers
3. A user query is converted into an embedding
4. Cosine similarity is computed between the query and all documents
5. The Top-5 most similar documents are ranked and displayed

---

## Model Used

- `all-MiniLM-L6-v2`
- 384-dimensional sentence embeddings
- Optimized for semantic similarity tasks
- Fast and lightweight transformer model

---

## Project Structure

```
endee-semantic-search/
│
├── search.py
├── README.md
```

---

## Setup and Execution

### 1. Clone the Repository

```
git clone https://github.com/ad8tea/endee-semantic-search.git
cd endee-semantic-search
```

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install sentence-transformers numpy
```

### 4. Run Semantic Search

```
python search.py
```

---

## Example Query

```
health
```

## Example Output

```
Top Matching Document:

Score: 0.5298
Text: Staying healthy requires regular exercise and proper nutrition.
```

---

## How It Works

- Documents are encoded into dense vectors using a transformer model.
- The query is converted into a vector.
- Cosine similarity is computed between the query vector and document vectors.
- The document with the highest similarity score (Top-1) is returned.

---

## Purpose
This project demonstrates:

Understanding of semantic search
Use of transformer embeddings
Vector similarity computation
Retrieval system design
Application of vector database concepts

---

## Future Improvements

- Integrate a vector database (e.g., Endee, FAISS)
- Add persistent embedding storage
- Implement REST API with FastAPI
- Extend to Retrieval-Augmented Generation (RAG)
- Add evaluation metrics for retrieval performance

---

## Author

Aditi Thakur
GitHub: https://github.com/ad8tea
