# Import the regular expressions module
import re

# Prompt the user to enter a name and store it in the 'name' variable
name = input("Name: ")

# Define a regular expression pattern that matches word characters
pattern = re.compile(r"\w+")

# Use the regular expression pattern to find all matches in the input 'name'
matches = pattern.findall(name)

# Print the list of matches
print(matches)

# Check if there are at least two matches (words)
if len(matches) >= 2:
    # Assign the first match to the 'last_name' variable
    last_name = matches[0]
    # Assign the last match to the 'first_name' variable
    first_name = matches[-1]
    
    # Print the last name and first name
    print("Last Name: ", last_name)
    print("First Name: ", first_name)
    
else:
    # Print an error message if there are not enough matches
    print("Error!!!")
