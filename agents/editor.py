class EditorAgent:
    def __init__(self, writer, fact_checker, headline_generator):
        self.writer = writer
        self.fact_checker = fact_checker
        self.headline_generator = headline_generator

    def review_and_finalize(self, summarized_content):
        print("Editor: Passing summarized content to Writer...")
        draft_article = self.writer.generate_article(summarized_content)

        print("Editor: Sending article to Fact-Checker...")
        checked_article, issues = self.fact_checker.verify_article(draft_article)

        print("Editor: Requesting headline...")
        headline = self.headline_generator.generate_headline(checked_article)

        final_article = {
            "headline": headline,
            "body": checked_article,
            "issues": issues
        }

        print("Editor: Article finalized.")
        return final_article

    # ✅ This makes it compatible with app.py
    def run_pipeline(self, summarized_content):
        return self.review_and_finalize(summarized_content)
