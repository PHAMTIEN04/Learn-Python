# locals và globals là các hàm sử dụng trong Python để truy cập đến các biến cục bộ hoặc toàn cục.

# locals() trả về một từ điển (dictionary) của các biến cục bộ trong phạm vi hiện tại. Ví dụ:
def my_func():
    x = 1
    y = 2
    print(locals())

my_func()

# Kết quả sẽ là một từ điển gồm các biến cục bộ x và y, như sau:

# {'x': 1, 'y': 2}

# Trong khi đó, globals() trả về một từ điển của các biến toàn cục trong phạm vi hiện tại. Ví dụ:

x = 1
y = 2

def my_func():
    z = 3
    print(globals()['x'])
    print(globals()['y'])

my_func()

# Khi chạy hàm my_func(), globals() sẽ trả về một từ điển gồm các biến toàn cục x và y, cho phép ta truy cập vào chúng bằng cách sử dụng khóa tương ứng, như sau:

# 1
# 2

# Tuy nhiên, cần lưu ý rằng việc truy cập trực tiếp vào các biến toàn cục có thể gây ra các vấn đề về bảo mật và khó khăn trong việc quản lý mã của bạn. 
# Do đó, nên sử dụng globals() một cách thận trọng và chỉ khi hoàn toàn cần thiết.

# Đọc Thêm Chi Tiết Tại : https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-bien-locals-va-globals-2656