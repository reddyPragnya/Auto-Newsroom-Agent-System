# agents/writer.py

from transformers import pipeline

class WriterAgent:
    def __init__(self, model_name="gpt2"):
        # Replace with more appropriate LLM for production
        self.generator = pipeline("text-generation", model="gpt2")




    def generate_article(self, summary: str) -> str:
        prompt = (
            f"Write a news article based on the following summary:\n\n"
            f"{summary}\n\n"
            f"Ensure the article is informative, neutral in tone, and follows a journalistic structure."
        )
        response = self.generator(prompt, max_length=512, do_sample=True, temperature=0.8)
        return response[0]["generated_text"].strip()
