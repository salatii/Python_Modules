from langdetect import detect, detect_langs
import sys

content = sys.argv[1] #content to detect language
print(detect_langs(content))