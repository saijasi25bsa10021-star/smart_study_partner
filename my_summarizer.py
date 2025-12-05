# summarizer.py
# Simple extractive summarizer (no external heavy models).
# Splits into sentences, scores sentences by word frequency, returns top N sentences in original order.

import re
from collections import Counter

# small stopword list (keeps model offline-friendly)
STOPWORDS = {
    "a","an","the","and","or","if","in","on","at","to","for","of","is","are","was","were",
    "be","been","being","by","with","that","this","these","those","it","its","as","from",
    "but","not","which","can","will","would","should","has","have","had","i","you","we","they",
    "he","she","them","his","her","their","my","your","our","us","so","than","then","about"
}

_SENT_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')

def sentence_tokenize(text):
    # basic sentence splitter
    text = text.strip()
    if not text:
        return []
    sentences = _SENT_SPLIT_RE.split(text)
    # keep sentences that have some alphabetic characters
    sentences = [s.strip() for s in sentences if re.search(r'[A-Za-z0-9]', s)]
    return sentences

def word_tokenize(text):
    # simple word tokenizer
    return re.findall(r"[A-Za-z0-9']+", text.lower())

def summarize(text, max_sentences=3):
    """
    Return an extractive summary composed of up to max_sentences.
    If text is short, returns the original text.
    """
    if not text or not text.strip():
        return ""

    sentences = sentence_tokenize(text)
    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    # build word frequency
    words = []
    for s in sentences:
        words.extend([w for w in word_tokenize(s) if w not in STOPWORDS])

    if not words:
        return " ".join(sentences[:max_sentences])

    freq = Counter(words)
    # score sentences by sum of word frequencies
    sent_scores = []
    for i, s in enumerate(sentences):
        s_words = [w for w in word_tokenize(s) if w not in STOPWORDS]
        score = sum(freq[w] for w in s_words)
        sent_scores.append((i, score, s))

    # pick top sentences by score
    sent_scores_sorted = sorted(sent_scores, key=lambda x: x[1], reverse=True)
    topk = sorted(sent_scores_sorted[:max_sentences], key=lambda x: x[0])  # restore original order
    summary = " ".join([s for (_, _, s) in topk])
    return summary
