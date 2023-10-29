from string01 import remove_duplicated_spaces  # Import the 'remove_duplicated_spaces' function from a module named 'string01'.

# Define a function 'capitalize_words' that capitalizes the first letter of each word in a string.
def capitalize_words(str_a):
    str_b = ""  # Initialize an empty string to store the result.

    # Check if the first character of the input string is a lowercase letter (between 'a' and 'z').
    if str_a[0] >= 'a' and str_a[0] <= 'z':
        str_b = str_b + chr(ord(str_a[0]) - 32)  # Convert the first character to uppercase and add it to the result.
    else:
        str_b = str_b + str_a[0]  # If not a lowercase letter, add the character to the result as is.

    check = False  # Initialize a flag 'check' to keep track of whether the previous character was a space.

    # Loop through the input string starting from the second character (index 1).
    for i in range(1, len(str_a)):
        # Check if the current character is not a space and 'check' is False.
        if str_a[i] != " " and not check:
            str_b = str_b + str_a[i]  # Add the character to the result as is.

        # Check if 'check' is True, indicating the previous character was a space.
        if check:
            # Check if the current character is a lowercase letter and convert it to uppercase, adding it to the result.
            if str_a[i] >= 'a' and str_a[i] <= 'z':
                str_b = str_b + chr(ord(str_a[i]) - 32)
            else:
                str_b = str_b + str_a[i]  # If not a lowercase letter, add the character to the result as is.

            check = False  # Reset the 'check' flag to False.

        # Check if the current character is a space, indicating the start of a new word.
        if str_a[i] == " ":
            str_b = str_b + str_a[i]  # Add the space to the result.
            check = True  # Set the 'check' flag to True to remember that the next character should be capitalized.

    return str_b  # Return the modified string with the first letter of each word capitalized.

# Example usage:
input_string = "Lap Trinh Python"
modified_string = capitalize_words(remove_duplicated_spaces(input_string))
print(modified_string)
