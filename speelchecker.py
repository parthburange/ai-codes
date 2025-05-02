from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Sample text with a typo
text = "This is an exmaple of a spell cheker."

# Split the text into words
words = text.split()

# Find and correct misspelled words
misspelled = spell.unknown(words)

for word in misspelled:
    corrected = spell.correction(word)
    print(f"Misspelled: {word} -> Corrected: {corrected}")
