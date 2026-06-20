import re
from typing import List


class FaqPreprocessor:
    """Clean and normalize text for FAQ similarity matching."""

    STOPWORDS = {
        "a", "an", "the", "and", "or", "is", "are", "was", "were", "in", "on", "for",
        "with", "to", "of", "by", "at", "from", "that", "this", "it", "as", "be",
        "can", "will", "do", "does", "did", "have", "has", "had", "but", "if", "not",
        "your", "you", "i", "we", "our", "my", "me", "so", "its", "these", "those",
        "how", "what", "when", "where", "why", "which", "who", "whom", "whose",
    }

    @classmethod
    def clean_text(cls, text: str) -> str:
        """Lowercase, remove punctuation, and normalize whitespace."""
        if not isinstance(text, str):
            return ""

        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        tokens = [token for token in text.split() if token and token not in cls.STOPWORDS]
        return " ".join(tokens)

    @classmethod
    def transform(cls, series) -> List[str]:
        """Apply text cleaning to a collection of texts."""
        return [cls.clean_text(text) for text in series]
