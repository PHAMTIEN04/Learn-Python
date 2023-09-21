# Import the regular expressions module
import re

# Prompt the user to input text
text = input("Text: ")

# Define a string containing punctuation characters that you want to remove from the text
Punctuation = "\.\,\;\?\!\:\[]\-"

# Create a regular expression pattern that matches sequences of characters that are not any of the specified punctuation characters.
pattern = re.compile(r"[^''\.\,\;\?\!\:]*")

# Use the pattern to find all non-overlapping matches in the input text
matches = pattern.findall(text)

# Print the list of matches, which should contain sequences of characters without the specified punctuation
print(matches)
