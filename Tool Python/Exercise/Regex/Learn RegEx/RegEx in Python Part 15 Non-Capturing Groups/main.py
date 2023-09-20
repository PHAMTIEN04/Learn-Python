import re

# Define the input text
txt = """
i love cats
i love dogs
"""

# Define a regular expression pattern to search for "i love cats" or "i love dogs"
pattern = re.compile(r"i love (cats|dogs)")

# Use the findall method to find all matching occurrences in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Iterate through the matches found by finditer and print details
for match in pattern.finditer(txt):
    print("Complete regex match (default):", match.group(0))
    print("Match captured by 1st group:", match.group(1))
    
# Modify the pattern to use a non-capturing group
pattern = re.compile("i love (?:cats|dogs)")

# Use findall again with the modified pattern
r = pattern.findall(txt)

# Print the results
print(r)
