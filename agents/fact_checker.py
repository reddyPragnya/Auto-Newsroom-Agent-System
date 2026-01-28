from transformers import pipeline

class FactCheckerAgent:
    def __init__(self, model_name="roberta-base"):
        self.checker = pipeline(
            "text-classification", 
            model=model_name, 
            tokenizer=model_name,
            truncation=True  # ✅ Force truncation
        )

    def verify_article(self, article_text: str):
        # Limit input to 400 characters just to be safe
        result = self.checker(article_text[:400])
        issues = []

        if result[0]["label"] == "LABEL_1":  # Example condition
            issues.append("Possible misinformation detected.")

        return article_text, issues