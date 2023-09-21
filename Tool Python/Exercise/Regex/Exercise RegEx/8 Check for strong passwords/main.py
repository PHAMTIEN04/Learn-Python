# Import the regular expressions module
import re

# Prompt the user to input a password
i_password = input("Password: ")

# Define a regular expression pattern for a strong password
# - ^: Start of the string
# - (?=.*[A-Z]): At least one uppercase letter
# - (?=.*[a-z]): At least one lowercase letter
# - (?=.*\d): At least one digit
# - (?=.*[@$!%*?&]): At least one special character among @$!%*?&
# - [A-Za-z\d@$!%*?&]{8,}: Allow only the specified characters and require a minimum length of 8 characters
# - $: End of the string
pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

# Use the pattern to check if the input password matches the criteria for a strong password
if pattern.match(i_password):
    print("Password Strong")  # If the password is strong, print a confirmation message
else:
    print("Password Weak")  # If the password is weak, print a message indicating that
