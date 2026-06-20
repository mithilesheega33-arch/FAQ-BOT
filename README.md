# FAQ Chatbot with NLP Similarity Matching

## Project Overview

This repository contains a production-quality FAQ chatbot built for a CodeAlpha internship project. The solution uses NLP-based similarity matching to map user questions to the best-matching FAQ answer.

Key features:
- Clean architecture with reusable modules
- Text preprocessing, dataset loading, model training, evaluation, and deployment guidance
- Both CLI and Flask API interfaces
- Unit tests for core behavior
- Beginner-friendly code and documentation

## Project Structure

- `src/` - core application modules and runtime interfaces
- `data/` - sample FAQ dataset for training and deployment
- `tests/` - unit tests for preprocessing and matching logic
- `requirements.txt` - Python dependencies

## Installation

1. Create a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Dataset Requirements

The chatbot expects a dataset file with the following columns:
- `question`
- `answer`
- optional: `category`, `tags`

We provide `data/faq_data.csv` as a sample dataset. For production, expand to 200+ FAQ pairs.

## Preprocessing Pipeline

1. Lowercase text
2. Remove punctuation and special characters
3. Remove stopwords
4. Normalize whitespace

This pipeline improves matching quality and reduces noise in user queries.

## Model Selection

The chatbot uses `TfidfVectorizer` and cosine similarity. It is a strong baseline for FAQ matching, easy to train, explainable, and fast for inference.

## Running the App

### CLI Example

```powershell
python src/app.py --mode cli --data data/faq_data.csv
```

### Flask API Example

```powershell
python src/app.py --mode api --data data/faq_data.csv
```

Then send a POST request to `http://127.0.0.1:5000/answer` with JSON:

```json
{"query": "How can I reset my password?"}
```

## Testing

Run unit tests with:

```powershell
pytest
```

## Expected Outputs

A typical query returns a structured JSON response like:

```json
{
  "answer": "To reset your password, go to the account settings page.",
  "confidence": 0.82,
  "matched_question": "How do I reset my password?"
}
```

## Future Enhancements

- Add transformer-based sentence embeddings for better semantic matching
- Expand to multi-language support
- Add a web dashboard with chat UX
- Add analytics for unanswered questions

## LinkedIn Project Summary

"Built an NLP-driven FAQ chatbot using TF-IDF similarity matching and an extensible Flask API. Designed a clean architecture with data preprocessing, reusable modules, and unit tests to support production-ready deployment."
