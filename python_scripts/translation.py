from transformers import pipeline
import sys

arg1 = sys.argv[1]
text = sys.argv[2]

if arg1 == 'de-en':
    translator_DE_EN = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en")
    translation = translator_DE_EN(text)
    print(translation)
elif arg1 == 'en-de':
    translator_EN_DE = pipeline("translation_en_to_de")
    translation = translator_EN_DE(text)
    print(translation)


