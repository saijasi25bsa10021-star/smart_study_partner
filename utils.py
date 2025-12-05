import pandas as pd
import random

def generate_mcqs(summary_text, n=5):
    sentences = summary_text.split(".")
    mcqs = []
    for i, sent in enumerate(sentences[:n]):
        if not sent.strip():
            continue
        mcqs.append({
            "question": f"What is described in this sentence? {sent[:50]}...",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })
    return mcqs

def evaluate_mcqs(mcqs, user_answers):
    score = 0
    for i, mcq in enumerate(mcqs):
        if user_answers.get(i) == mcq["answer"]:
            score += 1
    return score

def load_dataset(path):
    return pd.read_csv(path)

