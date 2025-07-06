# polipulse
# PoliPulse 🧠📄🇮🇳  
**AI-Powered Government Policy Analyzer**

PoliPulse is a full-stack AI web application that empowers users to upload government policy PDFs and receive instant summaries, sentiment analysis, and language insights. Designed for journalists, researchers, civil servants, and policy professionals, PoliPulse extracts, decodes, and delivers critical intelligence from policy documents.

---

## 🚀 Features

✅ Upload any government policy PDF  
✅ Extract text using PyMuPDF  
✅ Auto-detect document language  
✅ Summarize policy using `facebook/bart-large-cnn` (transformers)  
✅ Perform sentiment analysis using VADER  
✅ Deployed with **Streamlit Cloud**  
✅ Backend powered by **FastAPI**

---

## 🖥️ Demo

🟢 [**Live App** on Streamlit](https://tanvimaheshwari03-polipulse.streamlit.app)

---

## 🧰 Tech Stack

| Layer       | Technology                      |
|------------|----------------------------------|
| Frontend    | Streamlit                        |
| Backend     | FastAPI                          |
| NLP Models  | HuggingFace Transformers (`BART`) |
| PDF Parsing | PyMuPDF (`fitz`)                 |
| Sentiment   | VADER Sentiment Analyzer         |
| Language Detection | `langdetect`              |
| Deployment | Streamlit Cloud + GitHub          |

---

## 🗂️ Project Structure

```bash
polipulse/
│
├── backend/                  # FastAPI backend
│   ├── app.py                # Main FastAPI app
│   ├── summarizer.py         # HuggingFace summarizer logic
│   ├── sentiment_analyzer.py # VADER sentiment analysis
│   ├── fetch_policies.py     # Utility to fetch/read PDFs
│   └── requirements.txt      # Backend dependencies
│
├── frontend/                 # Streamlit frontend
│   ├── app.py                # Main UI app
│   └── requirements.txt      # Frontend dependencies
│
└── README.md
