# 🗞️ Auto-Newsroom Agent System

An intelligent, multi-agent AI system that automatically generates, fact-checks, and headlines** news articles from a given topic or summary. Powered by Hugging Face transformers and Flask, this full-stack project includes SQLite storage and a custom frontend.

Ideal for:
- AI product portfolios
- Journalism & NLP research
- Demonstrating agent-based system architectures

🧠 Agents
- WriterAgent: Generates the body of the news article using GPT-2 or BART.
  
- FactCheckerAgent: Performs basic fact-checking (extendable to use real-world APIs).
  
- HeadlineGeneratorAgent: Summarizes the article into a catchy headline.
  
- EditorAgent: Orchestrates the entire pipeline and stores the final output in SQLite.



🌐 Frontend UI
- `index.html`: Input form + live preview of results
- `app.js`: Handles AJAX POST requests to `/generate`
- `style.css`: Minimal styling


🚀 How to Run (GitHub Codespaces Compatible)

bash
# 1. Clone and open in GitHub Codespace
gh repo clone your-username/auto-newsroom-agent-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the Flask server
python app.py

# 4. Visit in browser
# Usually: https://[your-codespace-id]-5000.githubpreview.dev/




 Advanced Features (Future Work)
🧩 Add Fact Source Links

Enhance FactCheckerAgent to query sources via APIs like:

Google Knowledge Graph

Wikipedia API

OpenAI Web tools

🔄 Live RSS Feed Summarization

Pull live news RSS feeds (e.g., from BBC, Reuters) and pipe them into the writer pipeline.
⭐ Feedback Buttons

Let users rate or flag articles to improve the generation pipeline over time.

📬 Email Export or Share Links

Let users export or email articles.

🧠 Replace GPT-2 with Advanced Models

Like meta-llama/Llama-3-8B-Instruct, mistralai/Mixtral, or any HF-supported instruct model.



🙌 Credits
Built using:
🤗 Hugging Face Transformers
🐍 Python + Flask
🧠 OpenAI & Transformer models
💡 SQLite
💻 GitHub Codespaces


