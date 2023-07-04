from transformers import pipeline
import sys

content = sys.argv[1] #content for summary in english
classifier = pipeline("sentiment-analysis")
print(classifier(content))