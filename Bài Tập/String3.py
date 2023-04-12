# * ĐỊNH DẠNG CHUỖI BẰNG %

# %s : Giá Trị của Phương Thức __str__
s = "%s" %("WHAT")
print(s)

# %r : Giá Trị Của Phương Thức __repr__ 
r = "%r" %("Hi")
print(r)
# Note
# %s và %r nằm trong 1 class 
# %s thay thế cho giá trị của phương thức __str__ tạo nên đối tượng đó
# %r thì là phương thức __repr__

# %d : Giá Trị Của Một Số - Nếu là số thực thì sẽ chỉ lấy phần nguyên (Chuyển sang số nguyên)
d = "%d %d %d"  
result = d %(1,2,3)
print(result)
print("Dep trai never sai")



# "%.<Số Chữ Số Thập Phân>f" : Giá Trị Của Một Số - Nếu là số thì sẽ được chuyển sang số thực
t = 3.49999
f = "%.0f" %(t)
print(f)

# *ĐỊNH DẠNG CHUỖI BẰNG f (f-string)
# f"{variable} str " : tìm biến và lấy giá trị của biến đó
kteam = "Đánh Vần"
f_string = f"{kteam} abc"
print(f_string)
# Ứng dụng : rất tiện lợi và dễ dàng đọc code
# Có thể {{variable}} để note lại biến chưa định dạng
name =  str(input("Name: "))
address = str(input("Address: "))
phone =  str(input("Phone: "))
f_student = f"\nStudent: {{name}} \nAddress: {address}\nPhone: {phone}"
print(f_student)

#ĐỊNH DẠNG CHUỖI BẰNG FORMAT

# Cú Pháp : " {} " .format("")
# {Chỉ Số} format định dạng trong ngoặc nhọn bắt đầu từ chỉ số 0
for_mi = "a : {0}\nb : {1}" .format("Hi","Cau")
# {Tên variable} .format( variable = giá trị) có thể định dạng như variable
for_m = "a : {a}\nb : {b}" .format(a= 111,b = 222)
print(for_m)

#{:(c)^10} : Căn Lề Giữa
#{:(c)<10} : Căn Lề Trái
#{:(c)>10} : Căn Lề Phải
# Trong đó (c) là kí tự nếu không có thì mặc định là khoảng trắng
for_mo = "{:*^10}" .format("Hi")
print(for_mo)

#Ví dụ 
r1 = "+{:-^15}+{:-^15}+" .format("","")
r2 = "|{:^15}|{:^15}| " .format("STT","Name")
r_g = "|{:-^15}|{:-^15}|" .format("","")
r3 = "|{:^15}|{:^15}| " .format("1","Tiến")
r4 = "+{:-^15}+{:-^15}+" .format("","")


print(r1)
print(r2)
print(r_g)
print(r3)
print(r4)

the_end = "{:-^33}" .format("The End")
print(the_end)
