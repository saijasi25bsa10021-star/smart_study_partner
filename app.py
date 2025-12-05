
# app.py
import streamlit as st
import pandas as pd
import os
from summarizer_utils import summarize_text
from utils import generate_mcqs, evaluate_mcqs, load_dataset

st.set_page_config(page_title="Smart Study Partner", layout="centered")
st.title("📚 SMART_STUDY_PARTNER — Science & Math (SciQ)")

st.markdown("""
### This app will:
- Let you choose a subject/topic  
- Summarize the content  
- Generate MCQs  
- Evaluate your answers  
""")

# -----------------------------
# Load dataset
# -----------------------------
dataset_folder = "dataset"

def load_dataset_auto():
    try:
        files = os.listdir(dataset_folder)
        csv_files = [f for f in files if f.endswith(".csv")]
        if not csv_files:
            st.error("❌ No CSV file found in dataset folder.")
            return None
        file_path = os.path.join(dataset_folder, csv_files[0])
        df = pd.read_csv(file_path)
        st.success(f"Loaded dataset: **{csv_files[0]}** with {len(df)} rows")
        return df
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return None

df = load_dataset_auto()
if df is None:
    st.stop()

# -----------------------------
# User input
# -----------------------------
topic = st.text_input("Enter the topic you want to study:")

if topic:
    filtered_rows = df[df.apply(lambda row: topic.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    if filtered_rows.empty:
        st.warning("Topic not found in dataset.")
    else:
        text_data = filtered_rows.iloc[0].astype(str).str.cat(sep=" ")
        st.subheader("📌 Summary")
        summary = summarize_text(text_data)
        st.write(summary)

        st.subheader("📝 MCQ Quiz")
        mcqs = generate_mcqs(summary)
        answers = {}
        for i, mcq in enumerate(mcqs):
            st.write(f"**Q{i+1}: {mcq['question']}**")
            answers[i] = st.radio("Select answer:", mcq['options'], key=f"q{i}")

        if st.button("Submit"):
            score = evaluate_mcqs(mcqs, answers)
            st.success(f"Your Score: **{score}/{len(mcqs)}**")
