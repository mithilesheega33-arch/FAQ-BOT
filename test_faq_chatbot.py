import pytest

from src.faq_bot import FaqChatbot
from src.preprocessor import FaqPreprocessor


@pytest.fixture
def faq_bot():
    bot = FaqChatbot(threshold=0.1)
    faqs = [
        {"question": "How do I reset my password?", "answer": "Visit account settings to reset your password."},
        {"question": "What is your refund policy?", "answer": "Refunds are available within 30 days of purchase."},
    ]
    bot.fit(faqs)
    return bot


def test_clean_text_removes_punctuation_and_stopwords():
    result = FaqPreprocessor.clean_text("How do I reset my password?")
    assert "reset" in result
    assert "password" in result
    assert "how" not in result
    assert "do" not in result


def test_predict_returns_high_confidence_answer(faq_bot):
    response = faq_bot.predict("How can I reset my password")
    assert response["answer"] == "Visit account settings to reset your password."
    assert response["confidence"] > 0.2


def test_predict_returns_fallback_for_unknown_query(faq_bot):
    response = faq_bot.predict("Can I fly to Mars?")
    assert "couldn't find" in response["answer"].lower()
    assert response["confidence"] >= 0.0


def test_predict_empty_query_returns_error_message(faq_bot):
    response = faq_bot.predict("")
    assert response["confidence"] == 0.0
    assert "valid question" in response["answer"].lower()
