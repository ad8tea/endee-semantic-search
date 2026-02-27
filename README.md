# Semantic Search System using Endee Vector Database

## Problem Statement

Traditional keyword-based search systems fail when users phrase queries differently from how documents are written. This leads to missing relevant results even when the content is semantically related.

This project implements a semantic search system that retrieves documents based on meaning rather than exact word matches using transformer-based embeddings and the Endee vector database.

---

## System Architecture

### Indexing Pipeline

1. Load text documents  
2. Generate vector embeddings using the `all-MiniLM-L6-v2` model from sentence-transformers  
3. Store embeddings in the Endee vector database  

### Query Pipeline

1. Convert user query into an embedding  
2. Perform cosine similarity search in Endee  
3. Retrieve Top-5 most similar documents ranked by similarity score  

---

## Design Decisions

- **all-MiniLM-L6-v2** was chosen because it is lightweight, fast, and provides strong semantic performance for small to medium-sized datasets.  
- **Cosine similarity** is used because it works effectively for comparing normalized embedding vectors.  
- **Endee** is used as the core vector database for efficient similarity search and scalable retrieval operations.  

---

## Features

- Semantic search beyond keyword matching  
- Vector storage and retrieval using Endee  
- Top-5 ranked search results  
- Similarity score output  

---

## Tech Stack

- Python  
- sentence-transformers  
- Endee Vector Database  

---

## Setup and Execution

### Clone the Repository
