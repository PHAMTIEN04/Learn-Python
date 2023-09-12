import re

# Text containing the sentence
txt = """
the most common conjunctions are and, or and but.
"""

# Define a regular expression pattern to find "and", "or", or "the"
pattern = re.compile(r"(and|or|the)")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Another text
txt = """
What is your name?
Who is that guy?
"""

# Define a regular expression pattern to find "What is" or "Who is"
pattern = re.compile(r"What|Who is")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Define a regular expression pattern to find "What" or "Who" followed by "is"
pattern = re.compile("(What|Who) (is)")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)
