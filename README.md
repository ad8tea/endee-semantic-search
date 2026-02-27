# Semantic Search System using Transformer Embeddings

## Project Overview

This project implements a semantic search system using transformer-based embeddings to retrieve the most relevant documents based on meaning rather than keyword matching.

The system encodes text documents into vector embeddings and performs similarity search using cosine similarity to return the Top-5 most relevant results for a user query.

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
├── data/
│   └── sample_docs/
│       ├── doc1.txt
│       ├── doc2.txt
│       ├── doc3.txt
│       ├── doc4.txt
│       └── doc5.txt
│
├── search.py
├── requirements.txt
└── README.md
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
pip install -r requirements.txt
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
Top Matching Documents:

Document 1: doc1.txt
Similarity Score: 0.5290

Document 2: doc3.txt
Similarity Score: 0.2851

Document 3: doc2.txt
Similarity Score: 0.1480

Document 4: doc5.txt
Similarity Score: 0.0386

Document 5: doc4.txt
Similarity Score: 0.0159
```

---

## Technical Details

- Embeddings generated using SentenceTransformers
- Cosine similarity used for ranking
- NumPy used for vector computations
- Fully local implementation (no external API required)

---

## Future Improvements

- Integrate a vector database (e.g., Endee, FAISS)
- Add persistent embedding storage
- Implement REST API with FastAPI
- Extend to Retrieval-Augmented Generation (RAG)
- Add evaluation metrics for retrieval performance

---

## Author

Aditi

AI / Machine Learning Enthusiast
