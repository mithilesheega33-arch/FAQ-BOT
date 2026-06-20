# FAQ Chatbot Architecture

## Overview

The project follows a modular architecture:
- `src/data_loader.py` handles dataset ingestion and validation.
- `src/preprocessor.py` normalizes text for similarity matching.
- `src/faq_bot.py` builds and queries an FAQ knowledge base using TF-IDF.
- `src/app.py` exposes CLI and Flask API interfaces.

## Data Flow

1. Load FAQ dataset
2. Preprocess question text
3. Build TF-IDF vectors
4. Accept query and clean it
5. Compute cosine similarity with FAQ vectors
6. Return best answer or fallback message

## Error Handling

- Invalid dataset path raises `FileNotFoundError`
- Unsupported dataset formats raise `ValueError`
- Empty queries return a friendly prompt
- API validates JSON request structure

## Deployment Strategy

- Use a Python virtual environment
- Install dependencies from `requirements.txt`
- Run CLI or Flask API
- Add containerization later with Docker for staging/production
