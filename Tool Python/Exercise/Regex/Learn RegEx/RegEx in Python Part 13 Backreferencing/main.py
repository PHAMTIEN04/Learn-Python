import re

# Sample text
txt = """
hello hello hello
how are you
bye bye
"""

# Create a regular expression pattern that looks for repeated words separated by a space
pattern = re.compile(r"(\w+) \1")

# Find all instances of the pattern in the text
matches = pattern.findall(txt)

# Print the matches
print(matches)

# Sample text with dates
txt = """
today is 23/02/2019.
yesterday was 22/02/2019.
tomorrow is 24/02/2019.
"""

# Create a regular expression pattern that matches date strings in the format "dd/mm/yyyy"
pattern = re.compile("(\d{2})\/(\d{2})\/(\d{4})")

# Find all date matches in the text
date_matches = pattern.findall(txt)

# Print the date matches
print(date_matches)

# Replace the date format from "dd/mm/yyyy" to "yyyy-mm-dd" using captured groups
newtxt = pattern.sub(r"\3-\2-\1", txt)

# Print the modified text
print(newtxt)
