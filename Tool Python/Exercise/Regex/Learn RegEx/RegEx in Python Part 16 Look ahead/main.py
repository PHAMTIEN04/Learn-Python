# Import the necessary modules
import re
from utils import highlight_regex_matches

# Define the input text
txt = "i love python, i love regex"

# Define a regular expression pattern to find "love" followed by "regex" using a positive lookahead assertion
pattern = re.compile(r"love (?=regex)")

# Use findall to find all occurrences of the pattern in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Define a new input text
txt = "My favorite colors are red, green, and blue."

# Define a regular expression pattern to find words followed by a comma or period using a positive lookahead assertion
pattern = re.compile(r"\w+(?=,|\.)")

# Use findall to find all occurrences of the pattern in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Reassign the input text
txt = "i love python, i love regex"

# Define a regular expression pattern to find "love" not followed by "regex" using a negative lookahead assertion
pattern = re.compile(r"love (?!regex)")

# Use findall to find all occurrences of the pattern in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Call a function to highlight the matches found by the pattern in the text
highlight_regex_matches(pattern, txt)
