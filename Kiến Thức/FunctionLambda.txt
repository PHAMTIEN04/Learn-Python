# Trong Python, function là một loại dữ liệu có thể gán cho các biến, truyền vào như tham số và được trả về từ một function khác. Ngoài ra, Python còn hỗ trợ loại hàm đặc biệt được gọi là Lambda function.

# Lambda function, hay còn gọi là anonymous function (hàm vô danh), là một loại function không có tên và thường chỉ được sử dụng trong một phạm vi hẹp. Ý nghĩa của Lambda function là tạo ra một hàm ngắn gọn, dễ đọc và dễ hiểu hơn những hàm thông thường.

# Cấu trúc chung của Lambda function trong Python:


lambda arguments : expression
# Trong đó:

# arguments: là danh sách các tham số của hàm.
# expression: là biểu thức mà hàm sẽ trả về khi được gọi.
# Ví dụ, đoạn code sau tạo một Lambda function tính bình phương của một số:


squares = lambda x : x**2
print(squares(5)) # output: 25
# Ở đây, function squares chính là một Lambda function, nhận một tham số x và trả về bình phương của nó.
# Ta có thể dùng Lambda function để định nghĩa hàm bên trong một hàm khác hoặc sử dụng nó để lọc dữ liệu trong một list, dictionary hoặc set.

# Hy vọng giúp được cho bạn!


# Đọc thêm chi tiết tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python---lambda-2728