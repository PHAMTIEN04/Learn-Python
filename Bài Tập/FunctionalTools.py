# Trong Python, module functools cung cấp cho chúng ta nhiều công cụ hỗ trợ việc lập trình hàm trong Python. 
# Các chức năng này bao gồm cache, reduce, partial, wraps, singledispatch và một số công cụ khác.

# Dưới đây là giải thích về một số chức năng quan trọng của module functools:

# cache: Chức năng này sử dụng memoization để lưu kết quả của một function. Khi function được gọi, nó kiểm tra xem kết quả đã được lưu trữ trong bộ nhớ cache 
# hay không. Nếu tồn tại, nó sẽ trả lại kết quả đó mà không cần thực hiện tính toán lại.
# reduce: Chức năng này áp dụng một function cho từng phần tử trong một iterable để giảm các phần tử đó thành một giá trị duy nhất.
# partial: Chức năng này cho phép ta tạo ra một phiên bản mới của một function bằng cách giữ nguyên một số tham số ban đầu. Khi gọi function mới, chúng ta 
# chỉ cần truyền vào các tham số còn lại.
# wraps: Chức năng này được sử dụng để giữ lại thông tin metadata quan trọng khi sử dụng decorator để thay đổi function ban đầu. Thông tin metadata này 
# bao gồm tên, module, docstring,... của function.
# singledispatch: Chức năng này cho phép ta định nghĩa một hàm trong một kiểu dữ liệu và mở rộng nó cho các kiểu dữ liệu khác.
# Module functools là một công cụ hữu ích trong việc lập trình hàm trong Python. Hy vọng những giải thích trên sẽ giúp bạn hiểu rõ hơn về những tính năng 
# quan trọng của module này
def dk(x):
    return x + 1

lst = [1,2,-3,-4]
print(list(map(dk,lst)))


def mymap(func,iterable):
    for x in iterable:
        yield func(x)
        
print(list(map(dk,lst)))

func= lambda x : x > 0

print(list(filter(func,lst)))

from functools import reduce
add = lambda x,y : x+y
kteam = [1,2,3,4]

print(reduce(add,kteam))

# Đọc thêm chi tiết tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-functional-tools-2729