import argparse
import json
import os
from typing import Dict, List

from flask import Flask, jsonify, request

from src.data_loader import FaqDataLoader
from src.faq_bot import FaqChatbot


def build_chatbot(data_path: str, threshold: float = 0.45) -> FaqChatbot:
    loader = FaqDataLoader(data_path)
    df = loader.load()
    faqs = df.to_dict(orient="records")
    bot = FaqChatbot(threshold=threshold)
    bot.fit(faqs)
    return bot


def run_cli(bot: FaqChatbot):
    print("FAQ Chatbot CLI is ready. Type your question or 'exit' to quit.")
    while True:
        query = input("Question: ")
        if not query or query.strip().lower() == "exit":
            print("Goodbye!")
            break

        result = bot.predict(query)
        print(json.dumps(result, indent=2))


def create_app(bot: FaqChatbot) -> Flask:
    app = Flask(__name__)

    @app.route("/answer", methods=["POST"])
    def answer():
        payload = request.get_json(force=True, silent=True)
        if not payload or "query" not in payload:
            return jsonify({"error": "JSON body must include a 'query' field."}), 400

        query = payload["query"]
        if not isinstance(query, str) or not query.strip():
            return jsonify({"error": "Query must be a non-empty string."}), 400

        response = bot.predict(query)
        return jsonify(response)

    return app


def main():
    parser = argparse.ArgumentParser(description="Run the FAQ chatbot application.")
    parser.add_argument("--data", required=True, help="Path to the FAQ dataset (.csv or .json)")
    parser.add_argument("--mode", choices=["cli", "api"], default="cli", help="Run mode: cli or api")
    parser.add_argument("--threshold", type=float, default=0.45, help="Similarity threshold for answer matching")
    parser.add_argument("--host", default="127.0.0.1", help="Host for the Flask API")
    parser.add_argument("--port", type=int, default=5000, help="Port for the Flask API")
    args = parser.parse_args()

    if not os.path.exists(args.data):
        raise FileNotFoundError(f"Dataset not found: {args.data}")

    bot = build_chatbot(args.data, threshold=args.threshold)

    if args.mode == "cli":
        run_cli(bot)
    else:
        app = create_app(bot)
        app.run(host=args.host, port=args.port, debug=False)


if __name__ == "__main__":
    main()
