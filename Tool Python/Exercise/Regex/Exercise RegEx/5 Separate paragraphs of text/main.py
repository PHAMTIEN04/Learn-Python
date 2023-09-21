# Import the regular expressions module
import re

# Define a multi-line text with multiple occurrences
text = """
love your s love you

love your s love you

love your s love you
"""

# Create a regular expression pattern that matches one or more characters (non-greedy) followed by either two consecutive newline characters or the end of the string.
# The 're.DOTALL' flag allows the dot (.) to match newline characters as well.
pattern = re.compile(r".+?(?=\n\n|\Z)", re.DOTALL)

# Use the pattern to find all non-overlapping matches in the text
matches = pattern.findall(text)

# Iterate through the matches and print each one after stripping leading and trailing whitespace
for match in matches:
    print(match.strip())
