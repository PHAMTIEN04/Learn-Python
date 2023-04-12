# #  KIỂU DỮ LIỆU FUNTION TRONG PYTHON – Positional và keyword argument.

# # Positional argument và keyword argument
# # Với một hàm thông thường như sau

# def kteam(a, b):
#     pass # lệnh giữ chỗ.

# # Thì ta có thể pass argument vào cho hàm như sau

# kteam(3, 'Free Education')
# # 1
# # Trong ví dụ trên, hai giá trị là số 3 và chuỗi ‘Free Education’ gọi là positional argument.

# # Còn với trường hợp dưới đây

# kteam(a=3, b='Free Education')
# # 1
# # Thì hai giá trị trên (chính là số 3 và chuỗi ‘Free Education’) là những keyword argument.

# # Sau đây là những điều tuy nhỏ nhưng bạn cần phải biết. Khi pass argument theo positional argument. Thì các argument sẽ được gán LẦN LƯỢT cho các parameter. Riêng đối với keyword argument. Bạn đã tự mình gán giá trị cho các parameter. Vậy nên:

# def kteam(a, b):
#     print('a', a)
#     print('b', b)

# kteam(a=3,b=4)
# # a 3
# # b 4
# kteam(b=3,a=4)
# # a 4
# # b 3

# # Hai cách gọi hàm trên đều tương tự như nhau.

# # Một điều nữa là bạn không được phép để positional theo sau (follow) keyword.

# # Có nghĩa là bạn có thể pass argument vừa positional và keyword cùng một lúc được, nhưng những positional buộc phải đứng trước keyword.



# # Trường hợp ngớ ngẩn của Tèo sau đây sẽ cho bạn biết điều đó:

# def teo_with_sone(name, verb):
#     print('Teo', verb + 's', name)

# teo_with_sone('Python', 'love')
# # Teo loves Python
# teo_with_sone('HTML', verb='like')
# # Teo likes HTML
# teo_with_sone(verb='like', 'CSharp')
# #   File "<stdin>", line 1
# # SyntaxError: positional argument follows keyword argument
# # teo_with_sone(name='Java', 'hate')
# #   File "<stdin>", line 1
# # SyntaxError: positional argument follows keyword argument

# # Bắt buộc (force) Positional argument và keyword argument
# # Keyword argument
# # Trong Python, có một số hàm bắt chúng ta buộc phải pass argument một cách rõ ràng rành mạch như hàm sorted.

# sorted([3, 4, 1], reverse=True)
# [4, 3, 1]

# sorted([3, 4, 1], True)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: must use keyword argument for key function

# # Bạn thấy đấy, ta không thể pass argument cho parameter reverse theo positional argument.

# # Việc thiết kế này cũng rất tiện lợi vì nhiều trường hợp nhiều parameter cùng một lúc đều có default argument value. Hãy xem vấn đề sau đây mà Tèo mắc phải.

# # Tèo có một hàm

# def Teo(a, b=2, c=3, d=4):
#     f = (a + d) * (b + c)
#     print(f)

# Teo(1)
# # 25
# Teo(1, 2, 3, 5)

# # Tèo gọi hàm thì thấy kết quả theo đúng ý mình. Giờ Tèo muốn đổi giá trị của parameter d thành 5. Nên Tèo phải truyền lại các giá trị 2 và 3 cho các parameter b và c.

# # Vậy, ta có cách nào không phải truyền lại hai giá trị cho parameter b và c không?

# # Có, chính là keyword argument.

# Teo(1, d=5)
# # 30
# # 1
# # 2
# # Đôi lúc, chúng ta nên sử dụng keyword argument để tiện lợi và rõ ràng.

# # Python cho phép chúng ta tạo ra các parameter chỉ nhận giá  trị bằng việc pass argument theo kiểu keyword argument.

# # Cú pháp
# def function (*, key_arg1, key_arg2):

# # function-block

# # Khi tạo một hàm mà có một parameter *. Thì Python sẽ hiểu đó không phải là parameter mà chính là syntax để rồi nó biến các parameter sau * thành các keyword only argument (chỉ nhận giá trị theo kiểu keyword argument)

# # Ví dụ là dễ hiểu nhất!

# def kteam(pos_or_key_arg, *, key_arg1, key_arg2):
#     print(pos_or_key_arg)
#     print(key_arg1)
#     print(key_arg2)


# kteam(1, key_arg1=2, key_arg2='Kteam')
# # 1
# # 2
# # Kteam
# kteam(1, 2, key_arg2='Kteam')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: kteam() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given

# # kteam(1, 2, 'Kteam')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: kteam() takes 1 positional argument but 3 were given

# # Lưu ý: ta có thể thay thế dấu * bằng *identifier. Tuy nhiên phổ biến vẫn là *.

# # Positional argument
# # Bạn còn nhớ hàm input chứ? Kteam từng nói với bạn rằng cú pháp của hàm input có thể được viết như thế này.

# # input(prompt=None, /)

# # Dấu / chính là một syntax để force parameter prompt trở thành positional only argument. Có nghĩa là bạn chỉ có thể pass argument cho parameter prompt theo kiểu positional. Chính xác thì dấu / sẽ biến các parameter đứng trước nó thành positional only argument

# # Tuy nhiên Kteam sẽ không đi sâu vào positional argument vì ở phiên bản Python 3.6.X trở đi không hỗ trợ positional only argument.

# # Đọc thêm tại : https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python-positional-va-keyword-argument-2654


# Bài Tập
# Câu hỏi: Dùng hàm help để xem cú pháp của hàm sorted? Sau đó cho biết parameter nào là positional only? Parameter nào là keyword only?
print(help(sorted))
# Help on built-in function sorted in module builtins:

# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.

#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.

# None

# * iterable là positional only , key=None, reverse=False là keyword only
# Trong hàm sorted của Python, parameter positional only là iterable, được đặt trước dấu /. Điều này có nghĩa là khi sử dụng hàm,
# chúng ta không thể truyền giá trị cho iterable theo cách chỉ định keyword.
# Parameter keyword-only là key và reverse, được đặt sau dấu *. 
# Điều này có nghĩa là các tham số này phải được truyền vào hàm bằng cách sử dụng tên của chúng (ví dụ: sorted(my_list, key=my_function)), 
# và không thể được truyền vào bằng cách sử dụng vị trí của chúng.
# Việc sử dụng positional only hoặc keyword only được xác định bởi dấu "/" và "", tương ứng. Khi một tham số được đặt trước "/", 
# thì nó chỉ có thể được truyền đối số bằng cách sử dụng vị trí. Các tham số được đặt sau "" phải được thông qua bằng cách sử dụng keyword.

# Ví dụ
# def kteam(p_o, /,*, key_o):
#     print(p_o)
#     print(key_o)
    
# kteam(p_o=2,key_o=2)