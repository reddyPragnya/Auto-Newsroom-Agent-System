from transformers import pipeline

class HeadlineGeneratorAgent:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_headline(self, article_text: str) -> str:
        prompt = (
            "Generate a short, engaging headline for the following news article:\n\n"
            f"{article_text[:400]}\n\nHeadline:"
        )
        result = self.generator(
            prompt,
            max_new_tokens=12,   # fix here
            do_sample=True,
            temperature=0.9,
            pad_token_id=50256  #  GPT-2 safe padding
        )
        return result[0]["generated_text"].replace(prompt, "").strip()
