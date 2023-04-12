# Trong Python, một hàm là một khối mã được định nghĩa để thực hiện một công việc cụ thể và có thể được gọi từ bất kỳ đâu trong chương trình. 
# Cú pháp để định nghĩa một hàm trong Python như sau:

def function_name(parameters):
    # code block
    return value

# Trong đó:

# function_name là tên của hàm
# parameters (không bắt buộc) là các thông số được truyền vào cho hàm để thực hiện công việc
# code block là mã thực hiện công việc của hàm
# return (không bắt buộc) là giá trị được trả về khi hàm được gọi
# Để gọi một hàm, ta chỉ cần viết tên hàm và truyền giá trị cho các tham số nếu có.

# Ví dụ:
def calculate_sum(a, b):
    result = a + b
    return result

x = 5
y = 10
sum = calculate_sum(x, y)
print(sum)  # output: 15

# Trong ví dụ này, tôi đã định nghĩa hàm calculate_sum để tính tổng của hai số và trả về giá trị đó.
# Tại dòng 7, tôi đã gọi hàm calculate_sum với giá trị x và y là 5 và 10. Kết quả được trả về từ hàm là 15, 
# được lưu trong biến sum và được in ra màn hình tại dòng 8.

# Đọc Thêm Tại : https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-so-luoc-ve-ham-2653
