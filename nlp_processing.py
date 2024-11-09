from transformers import pipeline

def load_pipelines():
    sentiment_analyzer = pipeline("sentiment-analysis")
    summarizer = pipeline("summarization")
    return sentiment_analyzer, summarizer
