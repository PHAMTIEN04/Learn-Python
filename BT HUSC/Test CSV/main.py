import csv

# with open("test.csv", "a", newline='') as csv_test:
#     fieldname = ["One","Two","Three"]
#     csv_writer = csv.DictWriter(csv_test,fieldnames=fieldname, delimiter="-")
#     csv_writer.writeheader()
#     # Dữ liệu mới cần được thêm vào
#     # new_data = ["1", "2", "3"]

#     # Ghi dữ liệu vào file
#     # csv_writer.writerow(new_data)
    
#     # Không cần thêm dòng mới ở đây

# with open("new.csv","a",newline="") as csv_new:
#     csv_writer = csv.writer(csv_new,delimiter="-")   
#     fieldname = ["One","Two","Three"]
#     with open("test.csv","r") as csv_test:
#         csv_reader = csv.reader(csv_test,delimiter="-")
#         for line in csv_reader:
#             csv_writer.writerow(line) 
with open("new.csv","r+",newline="") as csv_n:
    csv_reader = csv.DictReader(csv_n,delimiter="-")
    header = csv_reader.fieldnames
    print(header)
    header.remove("One")
        # print(line)