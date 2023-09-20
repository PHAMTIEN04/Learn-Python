import re

# Define the filename to be read
filename = "text.txt"

# Uncomment the following code block to create and write data to the file
# list_data = ["file1.xml", "file1.txt", "file2.txt", "file15.xml", "file5.docx", "file60.txt", "file5.txt"]
# with open(filename, "w") as file:
#     for item in list_data:
#         file.write(str(item) + "\n")

# Read the content of the file
with open(filename, "r") as file:
    file_contents = file.read()

# Print the contents of the file
print(file_contents)

# Initialize an empty list to store matches
list_n = []

# Define a regular expression pattern to find lines containing "txt" in the content
reg = re.compile(r"(.*?txt)")
matches = reg.findall(file_contents)

# Print the matched lines
print(matches)
