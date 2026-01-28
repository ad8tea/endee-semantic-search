# Semantic Search Project using Endee Vector Database

## Project Overview

This project implements a semantic search system that uses transformer-based embeddings to convert text documents into vectors. The system leverages Endee as the vector database to store embeddings and perform similarity searches efficiently.

The goal is to demonstrate practical use of AI workflows such as semantic search using modern NLP models and vector databases.

## System Design and Technical Approach

- Text documents are loaded and converted into vector embeddings using the `sentence-transformers` library, specifically the `all-MiniLM-L6-v2` model.
- These embeddings are stored in Endee, a vector database designed for efficient similarity search.
- When a user inputs a search query, the system converts the query into a vector and compares it to the stored document embeddings using cosine similarity.
- The document with the highest similarity score is returned as the best match.

## How Endee is Used

Endee is used as the core vector database to store and query document embeddings. It allows for fast, scalable similarity searches, making it ideal for AI workflows like semantic search and retrieval-augmented generation (RAG).

## Setup and Execution Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ad8tea/endee-semantic-search.git
   cd endee-semantic-search
