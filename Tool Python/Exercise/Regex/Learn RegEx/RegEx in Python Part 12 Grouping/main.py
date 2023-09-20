import re
from utils import highlight_regex_matches

# Example 1: Matching "ab+" and "(ab)+" patterns in a string.
txt = "abbbbbabbbb"

# Compile regex patterns to find matches.
pattern1 = re.compile(r"ab+")   # Matches one or more 'ab' sequences.
pattern2 = re.compile(r"(ab)+") # Matches one or more 'ab' sequences as a group.

# Find all matches using both patterns.
r1 = pattern1.findall(txt)
r2 = pattern2.findall(txt)

# Print the results.
print(r1)  # Output: ['abbbbb', 'abbbb']
print(r2)  # Output: ['ab']

# Example 2: Matching names with or without "ram" or "sam".
txt = """
my name is ram
my name is sam
"""

# Compile regex patterns to find names with and without "ram" or "sam".
pattern1 = re.compile(r"my name is ram|sam")  # Matches the whole string.
pattern2 = re.compile(r"my name is (ram|sam)") # Matches only the name.

# Find all matches using both patterns.
r1 = pattern1.findall(txt)
r2 = pattern2.findall(txt)

# Print the results.
print(r1)  # Output: ['my name is ram', 'my name is sam']
print(r2)  # Output: ['ram', 'sam']

# Example 3: Extracting date components from a date string.
txt = "12/02/2019"

# Compile a regex pattern to capture day, month, and year.
pattern = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

# Search for the pattern in the text.
r = pattern.search(txt)

# Print the matched groups.
print(r.group(0))  # Output: '12/02/2019'
print(r.group(1))  # Output: '12'
print(r.group(2))  # Output: '02'
print(r.group(3))  # Output: '2019'

# Example 4: Extracting names from a multiline text.
txt = """
Name: Nikhil
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""

# Compile a regex pattern to capture names.
pattern = re.compile(r"Name: (.+)\n")

# Find all matches for names in the text.
r = pattern.findall(txt)

# Print the results.
print(r)  # Output: ['Nikhil', 'Ravi', 'Ram']
