# Được giới hạn bưởi cặp ngoặc ()
# Các phần tử của tuple được
# phân các bởi dấu ,
# tuple có khả năng chứa mọi giá trị
# Tốc độ truy xuất tuple nhanh hơn list
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# có thể dùng lạm key của dictionary

# Cách khởi tạo Tuple 
# Sử dụng cặp dấu () và đặt giá trị bên trong 
# Cú Pháp : (<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>)
tup = (1, 2, 3, 4)
print(tup)

empty_tup = () # khởi tạo tuple rỗng 
print(empty_tup)

# Bạn hãy chú ý khi khởi tạo tuple với một giá trị.
a = (8)
print(a) 
# trả về kết quả là 8 tại vì a không thuộc lớp tuple có thể check kiểu dữ liệu bằng cách type(a)
# Vì khi ta tính toán, hay sử dụng cặp ngoặc () để được ưu tiên.
#  Do đó, khi muốn khởi tạo một Tuple chỉ duy nhất một phần tử, ta phải thêm dấu 
# ,
#  vào sau giá trị đó, để báo cho Python biết, đây là Tuple.

# Sử Dụng Tuple Comprehension

# Với Tuple thì khái niệm Comprehension này không được áp dụng
tup_com = (value for value in range(3))
print(tup_com)
# Trả về <generator object <genexpr> at 0x039F5D20>
# Mà đó được coi là Generator Expression (Kteam sẽ giới thiệu trong tương lai).
# Đối tượng được tạo từ Generator Expression cũng là một dạng iterable.

# Sử Dụng Constructor Tuple

# Cú Pháp : tuple(iterable)
# Công dụng : Giống hoàn toàn với việc bạn sử dụng constructor List. Khác biệt duy nhất là constructor Tuple sẽ tạo ra một Tuple.

tup_con =  tuple([1, 2, 3])
print(tup_con)

str_tup = tuple('KTEAM')
print(str_tup)

Generator = ( i for i in range(10) if i % 2 == 0) 
print(tuple(Generator)) # bạn không cần phải cố gắng hiểu khi chưa rõ comprehension

# Một số toán tử
# Các toán tử của Tuple giống với toán tử của chuỗi. Nếu bạn đọc kĩ phần này ở bài List thì bạn sẽ thấy Kteam đề cập là toán tử của List chỉ là gần giống với toán tử của chuỗi.
# Lí do vì sao sẽ được giải thích trong bài sự khác biệt các toán tử của hash object (immutable như chuỗi, Tuple) và unhash object (mutable như List)

# Toán tử +
tup_total = (1,2,3) 
tup_total += (2,3)
print(tup_total)

# Toán tử *
tup_mul = (2,3)
tup_mul *= 3
print(tup_mul)

# Toán tử in 
tup_in = 2 in tup
print(tup_in)

# Indexing và cắt Tuple trong Python
# Indexing và cắt Tuple hoàn toàn tương tự như với kiểu dữ liệu List. (Nếu chưa biết về List bạn có thể tham khảo qua các bài về KIỂU DỮ LIỆU LIST TRONG PYTHON)
tup_l = len(tup)  # lấy số phần tử có trong tuple
print(tup_l)

print(tup[0])

print(tup[0:2])

print(tup[-1])

print(tup[::-1])

# Thay đổi nội dung Tuple trong Python
# Tuple và chuỗi đều là một dạng hash object (immutable). Do đó việc bạn muốn thay đổi nội dung của nó trên lí thuyết là không.
# tup[0] = "HOW"
# print(tup)
# Trả về lỗi
# Vì sao lại nói là trên lí thuyết? Bạn sẽ biết được ngay ở phần sau.

# Ma trận
# Nếu bạn nắm vững khái niệm này ở List. Thì xin chúc mừng bạn vì không phải đau đầu. Nó hoàn toàn tương tự.
tup_matrix = (((1,2,3),(2,3,4)),((9,5,2),(3,4,5)))
print(tup_matrix[0][0][1])

# Tuple có phải luôn luôn là một hash object?
# Như đã định nghĩa ở bài chuỗi, một hash object là một đối tượng bạn không thể thay đổi nội dung của nó. Và trong phần thay đổi nội dung Tuple, bạn cũng thấy ta không thể thay đổi giá trị 
# ở bên trong Tuple. Tuy nhiên, không phải lúc nào cũng vậy.
tup_check = ([1,2],3)
tup_check[0][1] = "How"
print(tup_check)
# Giá trị bên trong tuple đó là một List. Và, List là một unhash object. Suy ra, ta có thể thay đổi nội dung của nó.
# a đã thay đổi nội dung của Tuple bằng một cách đó là thay đổi nội dung của một phần tử trong Tuple.
# Vì thế, một Tuple sẽ được coi là một hash object khi nó chứa các phần tử đều là hash object.

# Các Phương Thức của Tuple

# count()
# Cú Pháp : <Tuple>.count(value)
# Công dụng: Trả về một số nguyên, chính là số lần xuất hiện của value trong Tuple.
tup_c = tup.count(1)
print(tup_c)

# index()
# Cú Pháp : <Tuple>.index(sub[, start[, end]])
# Công Dụng : Tương tự phương thức index của kiểu dữ liệu chuỗi.
tup_index = tup.index(1)
print(tup_index)


# Khi nào thì chọn Tuple thay cho List?
# Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:

# Tốc độ truy xuất của Tuple nhanh hơn so với List
# Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
# Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# Có thể dùng làm key của Dictonary (một kiểu dữ liệu sẽ được giới thiệu). Điều mà List không thể vì List là unhash object.
# Những điểm trên là những điều giúp bạn có thể cân nhắc việc chọn Tuple hay List để lưu dữ dữ liệu dưới một mảng.

# Bài Tập
# BT2
tup_bt2 = (1,2, [3,4])
tup_bt2[2][0] += [3]
print(tup_bt2)
# Đáp án b : TypeError: ‘tuple’ object does not support item assignment
