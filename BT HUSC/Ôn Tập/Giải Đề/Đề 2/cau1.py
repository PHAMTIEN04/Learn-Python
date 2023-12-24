# Take input for a string
str_i = str(input())

# Initialize an empty string to store alphabetic characters from the input string
str_n = ""

# Iterate through each character in the input string
for i in str_i:
    # Check if the character is an alphabetic character (either lowercase or uppercase)
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        str_n += i  # Append the alphabetic character to the new string

# Print the resulting string containing only alphabetic characters
print(str_n)
