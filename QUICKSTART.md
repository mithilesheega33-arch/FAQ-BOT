# Quick Start Guide

## Prerequisites
- Python 3.8+
- pip
- Virtual environment support

## 1. Setup Environment

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows
# source .venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 2. Prepare Data

Place your FAQ dataset in `data/faq_data.csv` with columns: `question`, `answer`

## 3. Run the Chatbot

### CLI Mode
```bash
python src/app.py --mode cli --data data/faq_data.csv
```

### API Mode
```bash
python src/app.py --mode api --data data/faq_data.csv
```

## 4. Run Tests
```bash
pytest -v
```

## 5. Deploy with Docker
```bash
docker build -t faq-chatbot:latest .
docker run -d -p 5000:5000 faq-chatbot:latest
```
