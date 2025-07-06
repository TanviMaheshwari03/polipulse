# backend/sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    scores = analyzer.polarity_scores(text)
    return {
        "positive": scores["pos"],
        "neutral": scores["neu"],
        "negative": scores["neg"],
        "compound": scores["compound"]
    }
