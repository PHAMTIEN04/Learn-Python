def string_e(value):
    # Reverse the input string until a space is encountered or the end of the string
    str_r = ""
    for i in reversed(value):
        if i == " ":
            break
        else:
            str_r += i
    
    # Reverse the reversed string to get the original order
    str_n = ""
    for i in reversed(str_r):
        str_n += i
        
    return str_n

# Create an empty list to store user input strings
list_name = []

# Continue taking user input until an empty string is entered
while True:
    str_n = str(input())
    if str_n == "":
        break
    else:
        list_name.append(str_n)

# Initialize a counter for the number of names that match "Anh"
cnt = 0

# Iterate through the list of names and check if the reversed last word is "Anh"
for i in list_name:
    if string_e(i) == "Anh":
        cnt += 1

# Print the count of names that match "Anh"
print("So luong sinh vien co ten [Anh] : {}".format(cnt))
