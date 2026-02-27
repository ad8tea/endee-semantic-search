Semantic Search System using Endee Vector Database
Problem Statement

Traditional keyword-based search systems fail when users phrase queries differently from how documents are written. This leads to missing relevant results even when the content is semantically related.

This project implements a semantic search system that retrieves documents based on meaning rather than exact word matches using transformer-based embeddings and the Endee vector database.

System Architecture
Indexing Pipeline

Load text documents

Generate vector embeddings using the all-MiniLM-L6-v2 model from sentence-transformers

Store embeddings in the Endee vector database

Query Pipeline

Convert user query into an embedding

Perform cosine similarity search in Endee

Retrieve Top-K most similar documents ranked by similarity score

Design Decisions

all-MiniLM-L6-v2 was chosen because it is lightweight, fast, and provides strong semantic performance for small to medium-sized datasets.

Cosine similarity is used as it works effectively for comparing normalized embedding vectors.

Endee is used as the core vector database for efficient similarity search and scalable retrieval operations.

Features

Semantic search beyond keyword matching

Vector storage and retrieval using Endee

Top-K ranked search results

Similarity score output

Tech Stack

Python

sentence-transformers

Endee Vector Database

Setup and Execution

Clone the repository:

git clone https://github.com/ad8tea/endee-semantic-search.git

cd endee-semantic-search

Install dependencies:

pip install -r requirements.txt

Run document indexing:

python index.py

Run semantic search:

python search.py

Example query:

AI applications in healthcare

Example output:

Document 1 – Score: 0.84
Document 2 – Score: 0.79
Document 3 – Score: 0.75

Future Improvements

Add evaluation metrics such as Precision@K

Add a web-based user interface

Extend the system to Retrieval-Augmented Generation (RAG)

Scale for larger datasets
