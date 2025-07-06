from transformers import pipeline, MarianMTModel, MarianTokenizer
from langdetect import detect

# Load English summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Translation model: Hindi → English
translation_model_name = "Helsinki-NLP/opus-mt-hi-en"
translator_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translator_model = MarianMTModel.from_pretrained(translation_model_name)

def translate_hi_to_en(text):
    inputs = translator_tokenizer(text, return_tensors="pt", padding=True)
    translated = translator_model.generate(**inputs)
    return translator_tokenizer.decode(translated[0], skip_special_tokens=True)

def summarize_text(text: str) -> str:
    if len(text) < 100:
        return "Text too short to summarize."

    try:
        lang = detect(text)
        if lang != "en":
            text = translate_hi_to_en(text)

        summary = summarizer(text, max_length=250, min_length=40, do_sample=False)[0]["summary_text"]
        return summary

    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"
