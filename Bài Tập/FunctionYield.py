# Yield trong Python là một keyword được sử dụng trong các generator function để tùy chỉnh hành vi lặp lại. Khi một generator được gọi, nó trả về một iterator object nhưng không bắt đầu chạy hàm ngay lập tức giống như các hàm khác. Từ khóa yield được sử dụng để trả về giá trị tiếp theo trong chuỗi mỗi khi phương thức next() của generator được gọi. Khi tất cả các giá trị đã được tạo ra, generator function sẽ raise StopIteration và tự động kết thúc.

# Dưới đây là ví dụ về cách định nghĩa một generator function bằng cách sử dụng từ khóa yield:

def my_generator():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
# Sử dụng generator
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# Đoạn mã trên sẽ xuất ra:


# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3



def sochan(n):
    for i in range(1,n+1):
        if i % 2 == 0 :
            print(i)

from time import *
n = int(input("Nhập N :"))
sochan(n)

def my_generator():
    for i in range(0,3):
        yield i
    
# Sử dụng generator

for i in my_generator():
    print(i)

# Đọc thêm chi tiết tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python---yield-2726