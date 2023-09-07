import re

# Match
pattern = re.compile("hello")

# Use match() to search for the pattern at the beginning of the string
p = pattern.match("hello world hello")
print(p.span())      # Prints the start and end positions of the match
print(p.start())     # Prints the start position of the match
print(p.end())       # Prints the end position of the match
print(p.group(0))    # Prints the matched string

# Use match() with a specified starting position
p = pattern.match("hello world hello", pos=11)
print(p.span())      # Prints the start and end positions of the match

# Search
pattern = re.compile("hello")

# Use search() to find the pattern anywhere in the string
p = pattern.search("hello word")
print(p.span())      # Prints the start and end positions of the match
print(p.group(0))    # Prints the matched string

# Findall
pattern = re.compile("hello")

# Use findall() to find all occurrences of the pattern
p = pattern.findall("hello world hello")
print(p)             # Prints a list of all matches

# Finditer
pattern = re.compile("hello")

# Use finditer() to find all occurrences of the pattern as iterator objects
p = pattern.finditer("hello world hello")

for i in p:
    print(i.group(0))  # Prints each matched string

# Example
txt = "this book costs $15"

# Define a pattern to match "$15"
pattern = re.compile(r"\$15")

# Use findall to find all matches in the text
p = pattern.findall(txt)

# Check if the result list is empty or not
if p == []:
    print("true")
else:
    print("false")

print(p)
