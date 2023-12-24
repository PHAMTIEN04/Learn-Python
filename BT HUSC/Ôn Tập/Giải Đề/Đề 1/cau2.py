# Create an empty list to store dictionaries representing courses
list_r = []

# Take input for the number of courses
n = int(input())

# Loop to input details for each course and append it to the list as a dictionary
for i in range(n):
    mahp = str(input())  # Course code
    tenhp = str(input())  # Course name
    sotc = int(input())  # Number of credit hours
    list_r.append({"mahp": mahp, "tenhp": tenhp, "sotc": sotc})

# Iterate through the list of courses and print details for those whose course code starts with "TIN"
for i in list_r:
    if i["mahp"][0:3] == "TIN":
        print(i)

# Take input for a string to search for in the course names
str_c = str(input())

# Iterate through the list of courses and print the course names that contain the input string
for i in list_r:
    if str_c in i["tenhp"]:
        print(i["tenhp"])
