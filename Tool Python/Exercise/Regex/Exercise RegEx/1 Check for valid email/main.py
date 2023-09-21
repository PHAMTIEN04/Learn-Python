# Import the regular expressions module
import re

## *Method 1

# Prompt the user to input an email address and store it in the 'i_mail' variable
i_mail = input("Input Email: ")

# Define a regular expression pattern to check for '@' or '.'
check_mail_kt = re.compile(r"\@|\.")
check_mail_kt = check_mail_kt.findall(i_mail)

# Define a regular expression pattern to extract components of the email address
check = re.compile(r"(.*?)@(.*?)\.(.*)")
check = check.findall(i_mail)

# Check if there are characters matching '@' or '.' in the input email
if len(check_mail_kt) != 0:
    # Check if there are exactly two characters, '@' and '.'
    if len(check_mail_kt) == 2 and (check_mail_kt[0] == '@' and check_mail_kt[1] == '.'):
        # Extract components of the email address
        kt_text = check[0][0]
        kt_one = check[0][1]
        kt_two = check[0][2]
        
        # Check if the components match a specific email format
        if kt_one == "example" and kt_two == "com":
            print("Email Confirm!!!")
        else:
            print("Email Error!!!")
    else:
        print("Email Error!!!")
else:
    print("Email Error!!!")

## *Method 2

# This section is commented out but provides an alternative method to validate email addresses.

# i_mail = input("Input Email: ")
# email_pattern = r"^[a-zA-Z0-9._%+-]+@example\.com$"
#
# if re.match(email_pattern, i_mail):
#     print("Email Confirm!!!")
# else:
#     print("Email Error!!!")
