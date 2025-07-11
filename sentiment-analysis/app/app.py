import streamlit as st
import requests

# ────────────────────────────────────────────────────────────────────────────────
# Streamlit Config
# ────────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Tweet Sentiment Analyzer", layout="centered")
st.title("💬 Twitter Sentiment Analyzer")
st.markdown("Predicts sentiment using a fine-tuned DistilBERT model served by FastAPI.")

# ────────────────────────────────────────────────────────────────────────────────
# Input Form
# ────────────────────────────────────────────────────────────────────────────────
with st.form("tweet_form"):
    tweet = st.text_area("Enter a tweet 👇", height=150)
    submitted = st.form_submit_button("Analyze")

# ────────────────────────────────────────────────────────────────────────────────
# API Call and Response Display
# ────────────────────────────────────────────────────────────────────────────────
if submitted:
    if not tweet.strip():
        st.warning("Please enter a tweet.")
    else:
        try:
            with st.spinner("Scoring…"):
                res = requests.post("http://127.0.0.1:8001/predict", json={"text": tweet}, timeout=10)
            res.raise_for_status()
            output = res.json()

            st.success(f"**Sentiment:** {output['sentiment'].capitalize()}")
            st.metric(label="Confidence", value=f"{output['confidence']*100:.2f}%")

        except Exception as e:
            st.error(f"API error: {e}")
            st.json({"text": tweet})  # For debugging
