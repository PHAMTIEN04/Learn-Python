import re

# Sample text
txt = "Nikhil Kumar"

# Create a regular expression pattern that captures two words as named groups
pattern = re.compile(r"(?P<first>\w+) (?P<last>\w+)")

# Search for the pattern in the text
pattern1 = pattern.search(txt)

# Print the first and last names using named groups
print(pattern1.group('first'), pattern1.group('last'))

# Swap the first and last names using backreferences
pattern2 = pattern.sub(r"\g<last> \g<first>", txt)

# Print the modified text with swapped names
print(pattern2)

# Another sample text
txt = "Jhonson Jhonson"

# Create a regular expression pattern that looks for repeated words with a named backreference
pattern3 = re.compile(r"(?P<first>\w+) (?P=first)")

# Find all instances of the pattern in the text
pattern3 = pattern3.findall(txt)

# Print the matches
print(pattern3)
