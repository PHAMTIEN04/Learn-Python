# Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.



# Một Set gồm các yếu tố sau:

# Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
# Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
# Set không chứa nhiều hơn 1 phần tử trùng lặp
# Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.

# Cách khởi tạo Set
# Sử dụng cặp  dấu ngoặc {} và đặt giá  trị bên trong
# Cú pháp: {<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>}
# Lưu ý: Khi khởi tạo bằng cách này, ít nhất phải có một giá trị.

set_ = {1, 2, 3, 4}
print(set_)
# {1, 2, 3, 4}
set_1 = {1, 1, 1} # các giá trị trùng lặp bị loại bỏ
print(set_1)
# {1}
empty_set = {}  # thử khởi tạo set rỗng
print(empty_set)
# {}
print(type(empty_set)) # không phải là set
# <class 'dict'>


# Sử dụng Set Comprehension
set_1 = {value for value in range(3)}
print (set_1)
# {0, 1, 2}

# Sử dụng constructor Set

# Cú Pháp : set(iterable)
# Công dụng: Giống hoàn toàn với việc bạn sử dụng constructor List. Khác biệt duy nhất là constructor Set sẽ tạo ra một Set.

set_1 = set((1, 2, 3))
print(set_1)
# {1, 2, 3}
set_2 = set('How Kteam')
print(set_2) # set không quan tâm đến vị trí của các phần tử
# {'o', ' ', 'a', 'm', 'H', 'K', 't', 'w', 'e'}
set_3 = set('aaaaaaaaa')
print(set_3)
# {'a'}
set_4 = set([1, 6, 8, 3, 1, 1, 3, 6])
print(set_4)
# {8, 1, 3, 6}
empty_set = set() # cách bạn tạo được empty set
print(empty_set)
# set()

# Một số toán tử với Set trong Python

# Toán tử in
# Cú Pháp : value in <Set>
# Công dụng : Kết quả trả về là True nếu value xuất hiện trong Set. Ngược lại sẽ là False
 
print(1 in {1, 2, 3})
# True
print(4 in {'a', 'How Kteam', 5})
# False 

# Toán tử -
# Cú pháp: <Set1> - <Set2>
# Công dụng : Kết quả trả về một Set gồm các phần tử chỉ tồn tại trong Set1 mà không tồn tại trong Set2

set1_text = {1,2,3,4}
set2_text = {2,3}
set_check_sub = set1_text - set2_text
print(set_check_sub)

# Toán tử &
# Cú Pháp : <Set1> & <Set2>
# Công dụng : Kết quả trả về là môt Set chứa các phần tử vừa tồn tại trong Set1 vừa tồn tại trong Set2

set_check_and = set1_text & set2_text
print(set_check_and)

# Toán tử | 
# Cú Pháp : <Set1> | <Set2>
# Công Dụng : Kết trả về là một Set chứa tất cả các phần tử tồn tại trong hai Set
set_check_or = set1_text | set2_text
print(set_check_or) 

# Toán tử ^
# Cú Pháp : <Set1> ^ <Set2>
# Công dụng : Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại một trong hai Set

set_check_xor = set1_text ^ set2_text 
print(set_check_xor)

# Indexing và cắt Set trong Python
# Ở trên Kteam đã đề cập về việc set không quan tâm đến vị trí của phần tử nằm trong set. Nên, việc indexing và cắt set trong Python không được hỗ trợ.
 
# Set không phải là một hash object
# Đúng như vậy! Điều đó có thể chứng minh theo hai cách:
# Ở ví dụ dưới, bạn cũng thấy, ta đã thay đổi nội dung của set nhưng id của set vẫn là id ban đầu

a = {1, 2}
print(id(a))
# 52255360
a.add(3)
print(id(a))
# 52255360

# Giải thích lí do tại sao lại có sự thay đổi ở set a? Cho giải pháp khắc phục?
# >>> a = {1, 2}
# >>> b = a
# >>> b.clear()
# >>> a # tại sao lại trở thành set rỗng?
# set()
# b đã tham chiếu tới địa chỉ của a => lúc này a và b có chung 1 địa chỉ khi ta thao tác clear trên b thì cũng đã gián tiếp clear a

