from transformers import pipeline
import sys

#Todo more Parameter for diffrent length -> SMS, E-Mail, Homepage
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
content = sys.argv[1] #content for keywords in english
print(summarizer(content, max_length=130, min_length=30, do_sample=False))