# Import the necessary modules
import re
from utils import highlight_regex_matches

# Define the input text
txt = "love regex or hate regex, can't ignore regex"

# Define a regular expression pattern to find "regex" preceded by "love" or "hate" using a positive lookbehind assertion and alternation (|) operator
pattern = re.compile(r"(?<=love|hate) regex")

# Use findall to find all occurrences of the pattern in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Call a function to highlight the matches found by the pattern in the text
highlight_regex_matches(pattern, txt)

# Reassign the input text
txt = "love regex or hate regex, can't ignore regex"

# Define a regular expression pattern to find "regex" not preceded by "love" or "hate" using a negative lookbehind assertion and alternation (|) operator
pattern = re.compile(r"(?<!love|hate) regex")

# Use findall again to find all occurrences of the pattern in the text
r = pattern.findall(txt)

# Print the results
print(r)
