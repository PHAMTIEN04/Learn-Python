# Import the regular expressions module
import re

# Prompt the user to input text, a search string, and a replacement string
text = input("Text: ")
find = input("Find: ")
replace = input("Replace: ")

# Create a regular expression pattern using the 'find' input within the 'format' method
pattern = re.compile(r"{}".format(find))

# Use the 'sub' method to replace all occurrences of 'find' with 'replace' in the 'text'
matches_r = pattern.sub(replace, text)

# Check if any replacements were made
if matches_r != text:
    print(matches_r)  # If replacements were made, print the modified text
else:
    print("No match found in the text.")  # If no matches were found, print a message indicating that
