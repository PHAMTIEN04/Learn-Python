def remove_duplicated_spaces(str_b):
    str_a = ""  # Initialize an empty string to store the result.

    # Check if the first character of the input string is not a space.
    if str_b[0] != " ":
        str_a = str_a + str_b[0]  # If not a space, add it to the result string.

    # Loop through the input string starting from the second character (index 1).
    for i in range(1, len(str_b)):
        # Check if the current character is not a space or the previous character is not a space.
        if str_b[i] != " " or str_b[i - 1] != " ":
            str_a = str_a + str_b[i]  # If conditions are met, add the character to the result string.

    # Check if the last character of the result string is a space.
    if str_a[-1] == " ":
        str_new = ""  # Initialize a new empty string to remove the trailing space.

        # Copy all characters from the result string to the new string, except the last character (the trailing space).
        for i in range(len(str_a) - 1):
            str_new = str_new + str_a[i]

        return str_new  # Return the new string with trailing spaces removed.
    else:
        return str_a  # If there are no trailing spaces, return the result string as is.

# Example usage:
# print(remove_duplicated_spaces("Lap Trinh Python3"))
