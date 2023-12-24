

list_r = []

while True:
    ten = str(input("Ten: "))
    sl = int(input("So luong: "))
    gb = int(input("Gia ban: "))
    if ten == "":
        break
    else:
        list_r.append({"Ten":ten,"SoLuong":sl,"GiaBan":gb})
    
for i in list_r:
    if i["SoLuong"] < 5:
        print("Mat hang so luong duoi 5:",i)

sum = 0    
for i in list_r:
    sum += i["SoLuong"] * i["GiaBan"]
    
print("Tong so tien hang:",sum)