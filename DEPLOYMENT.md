# Deployment Guide

## Local Development

### 1. Setup
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run Tests
```bash
pytest -v
```

### 3. Run Application
```bash
# CLI mode
python src/app.py --mode cli --data data/faq_data.csv

# API mode
python src/app.py --mode api --data data/faq_data.csv
```

## Docker Deployment

### 1. Build Image
```bash
docker build -t faq-chatbot:latest .
```

### 2. Run Container
```bash
docker run -d -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  --name faq-bot \
  faq-chatbot:latest
```

## Cloud Deployment (AWS Lambda, Heroku, Kubernetes)

See the full deployment guide in the docs directory for:
- AWS Lambda setup with SAM
- Heroku deployment
- Kubernetes manifests
- Environment configuration

## Monitoring & Logging

### Add Logging
```python
import logging
logger = logging.getLogger(__name__)
logger.info(f"Query received: {query}")
```

### Production Monitoring Stack
- **Metrics**: Prometheus
- **Logging**: ELK Stack
- **Tracing**: Jaeger
- **Alerts**: AlertManager

## Security Considerations

1. **Input Validation**: Sanitize user queries
2. **Rate Limiting**: Implement request throttling
3. **HTTPS**: Use SSL/TLS in production
4. **Authentication**: Add API key validation
5. **Data Privacy**: Comply with GDPR/CCPA

## Performance Optimization

1. **Caching**: Use Redis to cache responses
2. **Load Balancing**: Distribute requests across instances
3. **Async Processing**: Use async I/O for concurrent requests

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| 502 Bad Gateway | App crashed | Check logs, restart container |
| High latency | Large FAQ dataset | Implement caching layer |
| Low accuracy | Poor data quality | Expand/improve FAQ dataset |
