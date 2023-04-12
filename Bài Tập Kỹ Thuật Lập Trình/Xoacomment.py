input_string = input()  # Nhập xâu đầu vào
output_string = ""      # Khởi tạo xâu kết quả rỗng

comment_start = input_string.find("/*")  # Tìm vị trí bắt đầu của comment
while comment_start != -1:              # Nếu tìm thấy comment
    output_string += input_string[:comment_start]  # Thêm vào xâu kết quả từ đầu đến trước comment
    comment_end = input_string.find("*/", comment_start+2)  # Tìm vị trí kết thúc của comment
    if comment_end == -1:               # Nếu không tìm thấy vị trí kết thúc comment
        break                           # Thoát vòng lặp
    input_string = input_string[comment_end+2:]  # Cập nhật xâu đầu vào bằng phần còn lại sau comment
    comment_start = input_string.find("/*")      # Tìm vị trí bắt đầu của comment tiếp theo

output_string += input_string  # Thêm vào xâu kết quả phần còn lại sau khi đã xóa hết comment

print(output_string)  # In ra xâu kết quả đã xóa comment
# giá trị -1 thường được sử dụng để biểu diễn một kết quả không hợp lệ hoặc không tìm thấy.