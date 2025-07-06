# backend/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from backend.summarizer import summarize_text
from backend.sentiment_analyzer import analyze_sentiment
from backend.fetch_policies import fetch_recent_bills


app = FastAPI()

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request Schema ---
class TextRequest(BaseModel):
    text: str

# --- Summarization Endpoint ---
@app.post("/summarize/")
def summarize(request: TextRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}

# --- Sentiment Analysis Endpoint ---
@app.post("/sentiment/")
def sentiment(request: TextRequest):
    sentiment_result = analyze_sentiment(request.text)
    return {"sentiment": sentiment_result}

# --- Fetch PRS India Recent Bills Endpoint ---
@app.get("/recent-bills/")
def get_recent_bills():
    bills = fetch_recent_bills()
    return {"bills": bills}

@app.get("/")
def read_root():
    return JSONResponse({"message": "Welcome to PoliPulse Backend 🚀"})