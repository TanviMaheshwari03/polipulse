# frontend/app.py

import streamlit as st
import requests
import fitz  # PyMuPDF
from langdetect import detect

# ---- Page Config ----
st.set_page_config(page_title="PoliPulse", layout="centered")

# ---- Title and Description ----
st.title("🧠 PoliPulse")
st.subheader("Simplify Policies. Understand Public Sentiment.")
st.markdown(
    "Upload a policy PDF or paste a speech/document below. PoliPulse will auto-summarize and analyze public sentiment instantly using AI."
)

# ---- PDF Upload Handler ----
uploaded_pdf = st.file_uploader("📎 Upload a Policy PDF", type=["pdf"])

def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# ---- Input Handling ----
if uploaded_pdf:
    policy_text = extract_text_from_pdf(uploaded_pdf)
    st.success("✅ PDF uploaded and text extracted successfully!")
    st.text_area("📜 Extracted Text Preview", policy_text[:1000], height=250)
else:
    policy_text = st.text_area("✏️ Or paste policy text manually", height=300)

# ---- One Clean Button (Smart Behavior) ----
if st.button("🔍 Summarize & Analyze", key="analyze_button"):
    if policy_text:
        with st.spinner("Analyzing..."):
            try:
                # Detect Language
                lang = detect(policy_text)
                st.info(f"🌐 Detected language: `{lang}`")

                # API Calls
                summary_response = requests.post(
                    "http://localhost:8000/summarize/",
                    json={"text": policy_text}
                )
                sentiment_response = requests.post(
                    "http://localhost:8000/sentiment/",
                    json={"text": policy_text}
                )

                if summary_response.status_code == 200 and sentiment_response.status_code == 200:
                    # ---- Summary ----
                    st.subheader("📌 Summary")
                    st.success(summary_response.json()["summary"])

                    # ---- Language Translation Notice ----
                    if lang != "en":
                        st.caption("🌐 Original language was auto-translated to English before summarization.")

                    # ---- Sentiment ----
                    st.subheader("📊 Public Sentiment")
                    sentiment = sentiment_response.json()["sentiment"]

                    col1, col2, col3 = st.columns(3)
                    col1.metric("🟢 Positive", f"{sentiment['positive'] * 100:.1f}%")
                    col2.metric("🔵 Neutral", f"{sentiment['neutral'] * 100:.1f}%")
                    col3.metric("🔴 Negative", f"{sentiment['negative'] * 100:.1f}%")

                    st.caption(f"🧪 Compound Score: {sentiment['compound']:.2f}")
                else:
                    st.error("❌ Error from backend. Check FastAPI logs or try again.")
            except Exception as e:
                st.error(f"⚠️ Something went wrong: {str(e)}")
    else:
        st.warning("⚠️ Please upload a PDF or paste some text first.")

# ---- Divider ----
st.markdown("---")

# ---- Live Bills Feed ----
st.header("🗳️ Live Bills Feed (PRSIndia.org)")

if st.button("🔄 Load Latest Bills", key="load_bills"):
    with st.spinner("Fetching latest bills from PRSIndia..."):
        try:
            bills_response = requests.get("http://localhost:8000/recent-bills/")
            if bills_response.status_code == 200:
                bills = bills_response.json()["bills"]
                if not bills:
                    st.info("No new bills found.")
                else:
                    for bill in bills[:10]:
                        with st.container():
                            st.subheader(f"📄 {bill['title']}")
                            st.caption(f"📅 {bill['date']}")
                            st.markdown(f"[🔗 Read full bill]({bill['link']})", unsafe_allow_html=True)
                            st.markdown("---")
            else:
                st.error("Failed to fetch bills. Backend may be down.")
        except Exception as e:
            st.error(f"Error fetching bills: {str(e)}")
