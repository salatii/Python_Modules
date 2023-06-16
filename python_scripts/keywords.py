from keybert import KeyBERT
content = sys.argv[1] #content for keywords in english
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(content)
print(keywords)