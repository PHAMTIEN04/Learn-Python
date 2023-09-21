# Import the regular expressions module
import re

# Prompt the user to input text and keywords to find
text = input("Text: ")
find = input("Find keywords: ")

# Convert both the input text and keywords to lowercase to perform a case-insensitive search
text = text.lower()
find = find.lower()

# Create a regular expression pattern that matches the specified keywords as whole words using '\b' for word boundaries.
# The 're.escape' function is used to escape any special characters in the keywords.
pattern = re.compile(r"\b{}\b".format(re.escape(find)))

# Search for the pattern in the lowercase text
if pattern.search(text):
    print("Keyword found in the text.")  # If the keyword is found, print a message confirming it
else:
    print("Keyword not found in the text.")  # If the keyword is not found, print a message indicating that
