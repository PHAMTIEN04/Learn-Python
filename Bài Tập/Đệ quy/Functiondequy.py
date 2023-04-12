# Đệ quy là một kỹ thuật lập trình cho phép một hàm gọi chính nó trong quá trình thực thi. Khi sử dụng đệ quy, chúng ta giải quyết một vấn đề bằng cách chia nhỏ nó thành các vấn đề con, và tiếp tục giải quyết vấn đề con này bằng cách gọi lại chính hàm đó với dữ liệu đầu vào khác nhau.

# Để sử dụng đệ quy trong Python, bạn có thể định nghĩa một hàm và gọi lại nó trong thân hàm đó. Ví dụ, đây là một hàm đệ quy tính giai thừa của một số nguyên:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Hàm này tính giai thừa của một số nguyên n bằng cách kiểm tra nếu n bằng 0 thì trả về 1, nếu không, thì sử dụng đệ quy để tính giai thừa của số n-1, và nhân kết quả đó với n.

# Để sử dụng hàm này, bạn có thể gọi nó với đối số tương ứng như sau:


print(factorial(5)) # Kết quả: 120
# Lưu ý rằng khi sử dụng đệ quy, bạn cần phải thiết lập điều kiện dừng để tránh việc gọi hàm một cách vô tận và làm cho chương trình bị treo (hang).

# Đọc Chi Tiết Tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-de-quy-recursion-2731