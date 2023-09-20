import re

# Define the input text containing numbers
txt = "100 cats, 23 dogs, 3 rabbits"

# Define a regular expression pattern to find one or more digits (\d+)
pattern = re.compile(r"\d+")

# Use the sub() method to replace all matched digits with a hyphen (-) in the text
r = pattern.sub("-", txt)

# Print the result, which replaces all digits with hyphens
print(r)

# Define a regular expression pattern to find one or more digits (\d+)
pattern = re.compile(r"\d+")

# Use the subn() method to replace all matched digits with a hyphen (-) in the text
# The subn() method also returns the number of replacements made as a tuple
r = pattern.subn("-", txt)

# Print the result, which replaces all digits with hyphens and includes the count of replacements
print(r)
