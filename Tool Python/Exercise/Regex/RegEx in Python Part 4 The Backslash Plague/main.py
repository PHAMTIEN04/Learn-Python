import re

# Define a multi-line text containing Windows directory paths
txt = """
C:\Windows
C:\Python
C:\Windows\System32
"""

# Define a regex pattern to match the specific Windows directory path
r = re.compile(r"C:\\Windows\\System32")

# Find all occurrences of the pattern in the text
check = r.findall(txt)

# Print the list of matches (should contain ["C:\Windows\System32"])
print(check)

# Define a text containing a dollar sign followed by the number 15
txt = "$15"

# Define a regex pattern to match the specific text "$15"
r = re.compile(r"\$15")

# Find all occurrences of the pattern in the text
check = r.findall(txt)

# Print the list of matches (should contain ["$15"])
print(check)
