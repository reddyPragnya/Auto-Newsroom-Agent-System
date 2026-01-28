from flask import Flask, request, jsonify, send_from_directory
from agents.editor import EditorAgent
from agents.writer import WriterAgent
from agents.fact_checker import FactCheckerAgent
from agents.headline_generator import HeadlineGeneratorAgent
import sqlite3
import os



app = Flask(__name__, static_folder="frontend")

#   Initialize all agents
writer = WriterAgent()
fact_checker = FactCheckerAgent()
headline_generator = HeadlineGeneratorAgent()

#  Pass them to EditorAgent
editor = EditorAgent(writer, fact_checker, headline_generator)

DB_PATH = "articles.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            headline TEXT,
            body TEXT,
            issues TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    topic = data.get("topic", "")
    result = editor.run_pipeline(topic)

    # Save to DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO articles (topic, headline, body, issues) VALUES (?, ?, ?, ?)",
              (topic, result["headline"], result["body"], "; ".join(result["issues"])))
    conn.commit()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
