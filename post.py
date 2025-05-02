import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Process the sentence
doc = nlp(sentence)

# Print POS tags for each word
for token in doc:
    print(f'{token.text}: {token.pos_}')
