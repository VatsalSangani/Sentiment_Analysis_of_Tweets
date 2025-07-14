"""
main.py  –  FastAPI backend for Twitter-Sentiment project
---------------------------------------------------------
• Loads a fine-tuned DistilBERT model from Hugging Face Hub
• Exposes two endpoints:
    GET  /           → simple health-check
    POST /predict    → JSON { "text": "<tweet>" } → sentiment + confidence
"""

from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# ------------------------------------------------------------------#
# 1. Load model & tokenizer from Hugging Face Hub
# ------------------------------------------------------------------#
MODEL_HF_PATH = "brendvat/distilbert-ft"  # ✅ Use your actual HF repo path

tokenizer = AutoTokenizer.from_pretrained(MODEL_HF_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_HF_PATH)

label_map: dict[int, Literal["negative", "neutral", "positive"]] = {
    0: "negative",
    1: "neutral",
    2: "positive",
}

# ------------------------------------------------------------------#
# 2. FastAPI setup
# ------------------------------------------------------------------#
app = FastAPI(title="Tweet Sentiment API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow Streamlit/browser access
    allow_methods=["*"],
    allow_headers=["*"],
)

class TweetIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    sentiment: Literal["negative", "neutral", "positive"]
    confidence: float

@app.get("/", summary="Health-check")
def root() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOut, summary="Predict sentiment")
def predict_sentiment(tweet: TweetIn):
    if not tweet.text.strip():
        raise HTTPException(status_code=400, detail="Input text is empty.")

    inputs = tokenizer(tweet.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=1)[0]
        pred_idx = int(torch.argmax(probs).item())
        confidence = float(probs[pred_idx])

    return {
        "sentiment": label_map[pred_idx],
        "confidence": round(confidence, 4),
    }
