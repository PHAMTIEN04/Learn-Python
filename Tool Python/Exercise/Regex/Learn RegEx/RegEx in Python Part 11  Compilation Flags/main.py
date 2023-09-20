import re
from utils import highlight_regex_matches

# Using re.IGNORECASE or re.I to ignore case.
txt = """
The best thing about regex is that it makes the task of string manipulation so easy.
"""

# Compile a regex pattern to find all occurrences of "the" while ignoring case.
pattern = re.compile(r"the", flags=re.I)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Highlight regex matches in the text.
highlight_regex_matches(pattern, txt)

# Using re.MULTILINE or re.M to make begin/end boundary matchers (^, $) consider each line.
txt = """
A man was crossing the road.
Suddenly, a car passed before him in a very high speed.
He was terrified
And shocked.
"""

# Compile a regex pattern to match lines starting with "A" while considering each line.
pattern = re.compile(r"^A.+", flags=re.M)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Using re.DOTALL or re.S to make . match newline too.
pattern = re.compile(r"car.+", flags=re.S)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Using re.UNICODE or re.U to make {\w, \W, \b, \B} follow Unicode rules.
txt = "मुझे किताबें पढ़ना बहुत पसंद है।"

# Compile a regex pattern to find Unicode word characters.
pattern = re.compile(r"\w+")

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Using regex module for Unicode matching.
import regex

# Compile a regex pattern to find Unicode word characters using regex module.
pattern = regex.compile(r"\w+")

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Using re.ASCII or re.A to perform ASCII-only matching.
chars = ''.join(chr(i) for i in range(256))

# Compile a regex pattern to find ASCII word characters.
pattern = re.compile(r"\w+", flags=re.A)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(chars)
print(r)

# Using re.VERBOSE or re.X to allow comments in regex.
txt = """
This is a sample text123
"""

# Compile a regex pattern with comments to match words.
pattern = re.compile(r"""\w+    # Match one or more word characters""", flags=re.X)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)

# Highlight regex matches in the text.
highlight_regex_matches(pattern, txt)

# Using re.DEBUG to get information about the compiled pattern.
pattern = re.compile(r"\w+", flags=re.DEBUG)

# Find all matches of the pattern in the text and print them.
r = pattern.findall(txt)
print(r)
