from transformers import pipeline
import sys

content = sys.argv[1] #content for summary in english
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print(summarizer(content, max_length=130, min_length=30, do_sample=False))