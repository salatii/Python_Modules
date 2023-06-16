from transformers import pipeline
import sys

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en")
text = sys.argv[1]
translated = translator(text)
print(translated)
