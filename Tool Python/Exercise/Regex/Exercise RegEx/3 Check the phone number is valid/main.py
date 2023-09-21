# Import the regular expressions module
import re

# Prompt the user to input a phone number and store it in the 'i_phone' variable
i_phone = input("Phone: ")

# Define a regular expression pattern to match phone numbers in the format "(123) 456-7890" or "123-456-7890"
pattern = re.compile(r"\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}")

# Attempt to match the input phone number against the defined pattern
matches = pattern.match(i_phone)

# Check if a match was found
if matches:
    print("Phone Confirm !!!")  # If a match was found, print confirmation
else:
    print("Phone Error !!!")  # If no match was found, print an error message
