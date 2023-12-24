import csv 
from cau3 import Iris  # Assuming Iris class is defined in cau3 module

# Create an empty list to store Iris instances
list_iris = []

# Read data from the "Iris.csv" file and populate the list with Iris instances
with open("Iris.csv", "r") as read_csv:
    csv_read = csv.reader(read_csv)
    print(csv_read)  # Print the CSV reader object (for debugging purposes)
    cnt = 0
    for i in csv_read:
        if cnt > 0:
            # Create an Iris instance and append it to the list
            list_iris.append(Iris(float(i[0]), float(i[1]), float(i[2]), float(i[3]), str(i[4])))
        cnt = cnt + 1

# Create a new Iris instance X with specified attribute values and None for the class
X = Iris(7.1, 2.8, 6.4, 1.6, C=None)

# Calculate the distances between X and each Iris instance in the list
list_kc = []
for data in list_iris:
    list_kc.append(X.khoangcach(data))

# Sort the distances and print the sorted list
sort_list_kc = sorted(list_kc)
print(sort_list_kc)

# Select the three smallest distances
list_kc = sort_list_kc[0:3]
list_h = []

# Retrieve the class (C) values for the three closest instances
for data in list_iris:
    if X.khoangcach(data) == list_kc[0] or X.khoangcach(data) == list_kc[1] or X.khoangcach(data) == list_kc[2]:
        list_h.append(data.C)

# Count occurrences of each class in the list
h1 = "setosa"
h2 = "versicolor"
h3 = "virginica"

cnt_h1 = 0
cnt_h2 = 0
cnt_h3 = 0

for i in list_h:
    if i == h1:
        cnt_h1 += 1
    if i == h2:
        cnt_h2 += 1
    if i == h3:
        cnt_h3 += 1

# Determine the class for the instance X based on the majority class among the three closest instances
if cnt_h1 > cnt_h2 and cnt_h1 > cnt_h2:
    X.setKieuhoa(h1)
if cnt_h2 > cnt_h1 and cnt_h2 > cnt_h3:
    X.setKieuhoa(h2)
if cnt_h3 > cnt_h2 and cnt_h3 > cnt_h1: 
    X.setKieuhoa(h3)

# Print the determined class for instance X
print(X.C)
