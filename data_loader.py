import pandas as pd


class FaqDataLoader:
    """Load FAQ content from CSV or JSON for training the FAQ chatbot."""

    def __init__(self, path: str):
        self.path = path

    def load(self) -> pd.DataFrame:
        """Load dataset and validate required columns."""
        if self.path.endswith(".csv"):
            df = pd.read_csv(self.path)
        elif self.path.endswith(".json"):
            df = pd.read_json(self.path)
        else:
            raise ValueError("Unsupported file format. Use .csv or .json")

        required = {"question", "answer"}
        if not required.issubset(df.columns):
            raise ValueError(f"Dataset must contain columns: {required}")

        df = df.dropna(subset=["question", "answer"]).reset_index(drop=True)
        return df
