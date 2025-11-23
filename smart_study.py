from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import time

# -------------------------------------------------
# my messy little study helper 😎
# probably typed at 2 AM
# -------------------------------------------------

my_knowledge = {
    "photosynthesis": {
        "summary": "Plants make food from sunlight . They have this green stuff called chlorophyll that helps. Think of it like a mini solar kitchen in the leaves! 🍃",
        "questions": [
            "Chlorophyll… what does it even do?",
            "Why sunlight ? Why is it needed?",
            "Which gas do plants release when making food? (hint: we breathe it!)"
        ],
        "quiz": {
            "Where does photosynthesis mostly happen?": "Leaves"
        }
    },

    "machine learning": {
        "summary": "Machine learning = teaching computers to figure things out from examples instead of exact instructions 🤖. Cool, right?",
        "questions": [
            "Supervised learning… what comes to mind?",
            "Training vs testing data – explain in your words.",
            "Name 2 ML algorithms you know."
        ],
        "quiz": {
            "Which ML algorithm is usually used for classification?": "Decision Tree"
        }
    },

    "water cycle": {
        "summary": "Water keeps moving around 💧. Evaporates, forms clouds, rains, repeat… nature’s recycling system basically.",
        "questions": [
            "Evaporation – what does that mean to you?",
            "Condensation – explain it simply.",
            "Main stages of the water cycle?"
        ],
        "quiz": {
            "When rain forms, what’s that process called?": "Precipitation"
        }
    }
}

# -------------------------------------------------
# TF-IDF thingy to guess topics
# -------------------------------------------------
topics_list = list(my_knowledge.keys())
vec_tool = TfidfVectorizer()
topic_vecs = vec_tool.fit_transform(topics_list)

def guess_topic(user_text):
    """Tiny ML magic to find the topic the user means"""
    u_vec = vec_tool.transform([user_text])
    sims = cosine_similarity(u_vec, topic_vecs)
    return topics_list[sims.argmax()]

# -------------------------------------------------
# simulate typing like a human
# -------------------------------------------------
def human_print(msg, speed=0.02):
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(speed)
    print()

# -------------------------------------------------
# main program
# -------------------------------------------------
human_print("\nHeyyy! Welcome to your study buddy ")
human_print("We'll chat a bit, go through notes, maybe quiz a little… nothing too serious.\n")

user_topic = input("Which topic are you curious about today? ").strip().lower()
matched_topic = guess_topic(user_topic)

human_print(f"\nHmm… I think you mean **{matched_topic.title()}**. Cool choice! \n")

topic_info = my_knowledge[matched_topic]

# summary
human_print("Here's a quick summary for you:")
human_print(topic_info["summary"], speed=0.04)

# questions
human_print("\nSome things to think about while reading:")
for q in topic_info["questions"]:
    human_print("- " + q, speed=0.02)

# mini quiz
human_print("\nAlright, time for a tiny quiz! Don’t panic ")
score = 0
for q, ans in topic_info["quiz"].items():
    human_print(f"\nQ: {q}")
    a = input("Your answer: ").strip().lower()

    if a == ans.lower():
        human_print(random.choice([
            "Yesss! Correct! ",
            "Right on! ",
            "Bingo!  You got it!"
        ]))
        score += 1
    else:
        human_print(random.choice([
            f"Ah… not quite. The answer is {ans}. No worries, keep going! ",
            f"Oops! The right answer was {ans}. You’ll get it next time! ",
            f"Hmm… close! The correct answer is {ans}. Keep it up!"
        ]))

# wrap-up
human_print(f"\nAll done! Your score: {score}/{len(topic_info['quiz'])}")
human_print("Keep learning, stay curious, and go drink some water 💧\n")
