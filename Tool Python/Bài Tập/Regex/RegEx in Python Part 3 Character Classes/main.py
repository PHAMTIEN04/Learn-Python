import re

# TEXT
txt = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

# Define a regular expression pattern to match the word "license" or "licence"
r = re.compile(r"licen[cs]e")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches
print(check)

# Define a regular expression pattern to match any character except 'I'
r = re.compile(r"[^I]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches
print(check)

# Define a regular expression pattern to match four consecutive digits (year format)
r = re.compile(r"[1-9][0-9][0-9][0-9]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (years)
print(check)

# Predefined Character Classes

# Define a regular expression pattern to match four consecutive digits using \d
r = re.compile(r"[\d][\d][\d][\d]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (years)
print(check)

# Define a regular expression pattern to match four consecutive non-digits using \D
r = re.compile(r"[\D][\D][\D][\D]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (non-digit sequences)
print(check)

# Define a regular expression pattern to match whitespace characters using \s
r = re.compile(r"[\s]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (whitespace characters)
print(check)

# Define a regular expression pattern to match non-whitespace characters using \S
r = re.compile(r"[\S]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (non-whitespace characters)
print(check)

# Define a regular expression pattern to match word characters using \w
r = re.compile(r"[\w]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (word characters)
print(check)

# Define a regular expression pattern to match non-word characters using \W
r = re.compile(r"[\W]")

# Find all matches of the pattern in the given text
check = r.findall(txt)

# Print the list of matches (non-word characters)
print(check)



### TEST ###

# txt_new = ""
# cnt = False
# gg = 0
# for i in range(0,len(check)-1):

#     if check[i] == " " and check[i+1] == " " :
#         cnt = True
    
#     if cnt == False and gg == 0:
#         txt_new = txt_new + check[i]
#     elif cnt == False and gg == 1:
#         gg = 0
#     elif cnt == True:
#         gg = 1
#         cnt = False
        



    
# print(txt_new)