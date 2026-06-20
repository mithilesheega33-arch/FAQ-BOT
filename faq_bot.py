from typing import Dict, List, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessor import FaqPreprocessor


class FaqChatbot:
    """FAQ chatbot using TF-IDF similarity matching."""

    def __init__(self, threshold: float = 0.45):
        self.threshold = threshold
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.knowledge_base: List[Dict[str, str]] = []
        self.document_vectors = None

    def fit(self, faqs: List[Dict[str, str]]):
        """Build the vector representation of the FAQ knowledge base."""
        self.knowledge_base = [faq.copy() for faq in faqs]
        corpus = [FaqPreprocessor.clean_text(item["question"]) for item in self.knowledge_base]
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
        self.document_vectors = self.vectorizer.fit_transform(corpus)

    def _rank_responses(self, query: str) -> List[Dict[str, object]]:
        if self.vectorizer is None or self.document_vectors is None:
            raise RuntimeError("Chatbot must be fitted before calling predict.")

        clean_query = FaqPreprocessor.clean_text(query)
        query_vector = self.vectorizer.transform([clean_query])
        similarity_scores = cosine_similarity(query_vector, self.document_vectors).flatten()

        ranked = []
        for idx, score in enumerate(similarity_scores):
            ranked.append({
                "question": self.knowledge_base[idx]["question"],
                "answer": self.knowledge_base[idx]["answer"],
                "score": float(score),
            })

        ranked.sort(key=lambda item: item["score"], reverse=True)
        return ranked

    def predict(self, query: str) -> Dict[str, str]:
        """Return the best FAQ answer for the query or a fallback message."""
        if not query or not query.strip():
            return {
                "answer": "Please enter a valid question.",
                "confidence": 0.0,
            }

        ranked = self._rank_responses(query)
        top = ranked[0]
        if top["score"] < self.threshold:
            return {
                "answer": "I couldn't find a strong match. Can you rephrase your question?",
                "confidence": float(top["score"]),
            }

        return {
            "answer": top["answer"],
            "confidence": float(top["score"]),
            "matched_question": top["question"],
        }
