import re

# Text containing information about dogs
txt = """
I have 2 dogs. One dog is 1 year old and the other one is 2 years old. Both dogs are very cute! 
"""

# Define a regular expression pattern to find "dog" or "dogs"
pattern = re.compile(r"(dogs?)")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Text containing filenames
txt = """
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
file-1.txt
"""

# Define a regular expression pattern to find filenames ending with ".txt"
pattern = re.compile(r"file[\w-]*\.txt")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Text containing various file names
txt = """
file1.txt
file_one.txt
file09.txt
fil.txt
file23.xml
file.txt
"""

# Define a regular expression pattern to find filenames like "file{numbers}.txt"
pattern = re.compile(r"file\d+\.txt")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Text containing information about IPL seasons
txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015, and 2017.
"""

# Define a regular expression pattern to find four-digit years
pattern = re.compile(r"\d{4}")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Text containing various numbers
txt = """
123143
432
5657
4435
54
65111
"""

# Define a regular expression pattern to find numbers with 4 or more digits
pattern = re.compile(r"\d{4,}")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)

# Text containing phone numbers
txt = """
555-555-5555
555 555 5555
5555555555
"""

# Define a regular expression pattern to find phone numbers in various formats
pattern = re.compile(r"\d{3}[-\s]?\d{3}[-\s]?\d{4}")

# Use findall to find all occurrences of the pattern in the text
f_a = pattern.findall(txt)

# Print the list of matches
print(f_a)
