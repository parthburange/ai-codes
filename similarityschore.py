import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample sentences
sentence1 = "I love programming."
sentence2 = "Coding is fun."

# Convert sentences to spaCy objects
doc1 = nlp(sentence1)
doc2 = nlp(sentence2)

# Calculate similarity
similarity_score = doc1.similarity(doc2)

print(f"Similarity score: {similarity_score}")
