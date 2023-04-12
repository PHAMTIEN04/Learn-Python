# # Return là câu lệnh trong Python để trả về giá trị từ một hàm. 
# # Khi một hàm được gọi và thực hiện xong, nó có thể trả về kết quả bằng cách sử dụng câu lệnh return.
# # Giá trị được trả về có thể được sử dụng trong chương trình sau đó hoặc được in ra màn hình.

# # Ví dụ:

# # Hàm tính tổng của hai số
# def add_numbers(a, b):
#     result = a + b
#     return result
  
# # Sử dụng hàm add_numbers() và lấy giá trị trả về để in ra màn hình
# sum = add_numbers(5, 7)
# print("Tổng của hai số là:", sum)
# # Output:


# # Tổng của hai số là: 12
# # Trong ví dụ này, hàm add_numbers() tính tổng của hai số và trả về kết quả bằng câu lệnh return.
# # Giá trị trả về được lưu vào biến sum và in ra màn hình bằng lệnh print().

# # Đọc thêm chi tiết tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-return-2718

# Bài Tập 1

# hàm y = f(x) như sau
# y = pow(x,3) + (2*pow(x,2)-(4*x) + 1)

# định nghĩa hàm số đã cho
# def f(x):
#     return pow(x,3) + (2*pow(x,2)-(4*x) + 1)

# # Khởi tạo danh dách rỗng A và B
# A =[]
# B =[]

# # Danh sách các tuple đã cho
# lst = [(-5,-20), (-4,-15),  (-3,4), (-2,9),(-1,7),(0,1),(1,-7),(2,-9), (4,81),(5,130)]

# # Lặp qua từng tuple trong danh sách
# for i in lst:
#     x0,y0 = i # Unpack the tuple into x0 and y0
#     if y0 == f(x0):# Kiểm tra xem điểm có nằm trên đồ thị hay không
#         A.append(i)# Thêm điểm vào danh sách A nếu nó nằm trên đồ thị
#     else:
#         B.append(i)# Ngược lại thì thêm điểm vào danh sách B

# # Tính tổng tung độ của danh sách A và B      
# sum_a = sum([i[1] for i in A]) 
# sum_b = sum([i[1] for i in B])      

# # In ra hiệu tuyệt đối giữa sum_A và sum_B
# print(abs(sum_a - sum_b))

# Bài Tập 2
# định nghĩa hàm max
# def max_bt(a,b,c,d,e):
#     m = a
#     if m < b :
#         m = b
#     if m < c :
#         m = c 
#     if m < d:
#         m = d 
#     if m < e:
#         m = e
#     return 2*m -1

# a = 32
# b = 59
# c = 62
# d = 24
# e = 155

# print(max_bt(a,b,c,d,e))
    

