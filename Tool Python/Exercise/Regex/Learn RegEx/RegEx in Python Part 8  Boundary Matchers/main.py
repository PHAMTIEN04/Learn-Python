import re

# Define the input text
txt = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# Define a regular expression pattern to find specific words
pattern = re.compile(r"\b(and|or|the)\b")

# Find all matches in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Define a new input text
txt = """
Name:
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123 Name: ABC
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""

# Define a regular expression pattern to find lines starting with "Name:"
pattern = re.compile(r"^Name: \w+", flags=re.M)

# Find all matches in the text
r = pattern.findall(txt)

# Print the results
print(r)

# Define another input text
txt = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s!
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages
More recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# Define a regular expression pattern to find lines that do not end with a period
pattern = re.compile(r"^.+\w[^\.]$", flags=re.M)

# Find all matches in the text
r = pattern.findall(txt)

# Print the results
print(r)
