# Create an empty list to store dictionaries representing items
list_r = []

# Input loop to gather information about items (name, quantity, and price) until an empty name is entered
while True:
    ten = str(input("Ten: "))  # Item name
    sl = int(input("So luong: "))  # Quantity
    gb = int(input("Gia ban: "))  # Unit price
    
    # Check if the name is empty to break out of the loop
    if ten == "":
        break
    else:
        list_r.append({"Ten": ten, "SoLuong": sl, "GiaBan": gb})  # Append item details to the list

# Iterate through the list of items and print those with a quantity less than 5
for i in list_r:
    if i["SoLuong"] < 5:
        print("Mat hang so luong duoi 5:", i)

# Calculate the total cost by multiplying quantity and unit price for each item and summing them up
total_cost = 0
for i in list_r:
    total_cost += i["SoLuong"] * i["GiaBan"]

# Print the total cost
print("Tong so tien hang:", total_cost)
