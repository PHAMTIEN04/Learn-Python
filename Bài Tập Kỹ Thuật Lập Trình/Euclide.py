# Import the sqrt function from the math module
from math import sqrt

# Input data as a single line and split it into four values
input_data = input().split()

# Extract x and y coordinates of the first point
x = int(input_data[0])
y = int(input_data[1])

# Extract x and y coordinates of the second point
x1 = int(input_data[2])
y1 = int(input_data[3])

# Calculate the Euclidean distance between the two points
euclidean_distance = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

# Format the result to display it with 9 decimal places
euclidean_formatted = "{:.9f}".format(euclidean_distance)

# Print the formatted Euclidean distance
print(euclidean_formatted)
