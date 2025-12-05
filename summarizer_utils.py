
def summarize_text(text, n_sentences=2):
    """
    Simple summarizer: returns first n_sentences from the text.
    """
    sentences = text.split(".")
    summary = ". ".join([s.strip() for s in sentences if s.strip()][:n_sentences])
    if summary and not summary.endswith("."):
        summary += "."
    return summary
