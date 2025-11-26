import json
import os
def load_questions():
    file_path = os.path.join(os.path.dirname(__file__), "..", "question.json")
    file_path = os.path.abspath(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
