# Import the HOADON class from the "cau3" module
from cau3 import HOADON

# Create empty lists to store invoices and check for duplicate customer codes
list_hd = []
list_check = []

# Take input for the number of invoices (n)
n = int(input())

# Ensure the number of invoices is within a reasonable range
if n <= 50:
    # Loop to input details for each invoice and add it to the list as an instance of HOADON
    for i in range(n):
        mkh = str(input())   # Customer code
        ht = str(input())    # Customer name
        dc = str(input())    # Customer address
        csc = int(input())   # Previous electricity consumption
        csm = int(input())   # Current electricity consumption
        
        # Check if the customer code already exists in the list, if not, add the invoice
        if mkh not in list_check:
            list_check.append(mkh)
            list_hd.append(HOADON(mkh, ht, dc, csc, csm))
    
    # Sort the list of invoices based on electricity consumption (sldsd method)
    for i in range(len(list_hd) - 1):
        for j in range(i + 1, len(list_hd)):
            if list_hd[i].sldsd() > list_hd[j].sldsd():
                tmp = list_hd[i]
                list_hd[i] = list_hd[j]
                list_hd[j] = tmp
    
    # Take input for a customer code to search for in the list
    ma = str(input())
    check = False
    
    # Iterate through the list of invoices and display details for the specified customer code
    for i in list_hd:
        if ma == i.getmkh():
            i.hienthi()
            check = True
    
    # If the specified customer code is not found, print a message
    if not check:
        print("Không tồn tại khách hàng này")
    
    # Import the csv module and write the details of invoices with consumption greater than 100 to a CSV file
    import csv
    file = "hoadon.csv"
    with open(file, "+a", newline="") as file_csv:
        for i in list_hd:
            csv_writer = csv.writer(file_csv, delimiter=";")
            str_n = [i.mkh, i.ht, i.dc]
            if i.sldsd() > 100:
                csv_writer.writerow(str_n)
