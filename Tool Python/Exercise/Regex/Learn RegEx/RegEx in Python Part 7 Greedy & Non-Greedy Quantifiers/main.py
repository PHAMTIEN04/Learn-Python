import re

# The input text containing HTML tags
txt = "<html><head><title>Title</title>"

# Greedy Behavior

# Define a regular expression pattern to match HTML tags (greedy behavior)
pattern = re.compile(r"<.*>")
# Find all matches in the input text
r = pattern.findall(txt)
# Print the matches
print(r)

# Non-Greedy Behavior

# Define a regular expression pattern to match HTML tags (non-greedy behavior)
pattern = re.compile(r"<.*?>")
# Find all matches in the input text
r = pattern.findall(txt)
# Print the matches
print(r)
