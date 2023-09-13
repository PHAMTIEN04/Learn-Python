import re
from utils import highlight_regex_matches
# Define the input text with multiple lines
txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

# Define a regular expression pattern to split the text on newline characters
pattern = re.compile(r'\n')

# Split the text based on the pattern and store the result in 'r'
r = pattern.split(txt)

# Print the result, which splits the text into a list of lines
print(r)

# Define a regular expression pattern to split the text on non-word characters (punctuation and spaces)
pattern = re.compile(r'\W')

# Split the text based on the pattern and store the result in 'r'
r = pattern.split(txt)

# Print the result, which splits the text into a list of words
print(r)

# Define a regular expression pattern to split the text on non-word characters with a maximum of 3 splits
pattern = re.compile(r'\W')

# Split the text based on the pattern, limiting the number of splits to 3, and store the result in 'r'
r = pattern.split(txt, maxsplit=3)

# Print the result, which splits the text into a list of words with a maximum of 3 splits
print(r)



