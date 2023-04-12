# Khái niệm iteration trong Python
# Iteration là một khái niệm chung cho việc lấy từng phần tử một của một đối tượng nào đó, bất cứ khi nào bạn sử dụng vòng lặp hay kĩ thuật nào đó 
# để có được giá trị một nhóm phần tử thì đó chính là Iteration.

# Ví dụ: như bạn ăn một snack, bạn sẽ lấy từng miếng trong bọc snack ra ăn cho tới khi hết thì thôi. Bạn có thể coi việc lấy bánh là một vòng lặp. 
# Đương nhiên bạn cũng có thể chọn không lấy hết số bánh ra.

# Giới thiệu iterable object trong Python
# Iterable object là một object có phương thức __iter__ trả về một iterator, hoặc là một object có phương thức __getitem__ 
# cho phép bạn lấy bất cứ phần tử nào của nó bằng indexing ví dụ như Chuỗi, List, Tuple.

# Giới thiệu iterator object trong Python
# Iterator object đơn giản chỉ là một đối tượng mà cho phép ta lấy từng giá trị một của nó. Có nghĩa là bạn không thể lấy bất kì giá trị nào như ta hay làm với List hay Chuỗi.

# Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ trợ như file object sẽ có phương thức seek.
# Iterator sử dụng hàm next để lấy từng giá trị một. Và sẽ có lỗi StopIteration khi bạn sử dụng hàm next lên đối tượng đó trong khi nó hết giá trị đưa ra cho bạn.

# Các iterable object chưa phải là iterator. Khi sử dụng hàm iter sẽ trả về một iterator. Đây cũng chính là cách các vòng lặp hoạt động.

# Ví dụ minh họa:

iter1 = [x for x in range(3)] # thuộc lòng 3 giá trị của comprehension này
print(iter)
print(type(iter))
iter1 = (x for x in range(3)) # sử dụng () cho ra một generator expression – một iterator
print(iter)  
print(next(iter1))
print(next(iter1))
print(next(iter1))
# Nếu ta print thêm 1 lần nữa nó sẽ có lỗi tại vì nó đã hết giá trị
# print(next(iter)) => Báo lỗi, chỉ có 3 giá trị, và ta đã lấy hết

# File object cũng là một iterator. Bạn cũng có thể sử dụng cách này để đọc file.
lst = [6, 3, 7, 'kteam', 3.9, [0, 2, 3]]
iter_listaaa = iter(lst)  # iter_list là một iterator tạo từ list
print(next(iter_listaaa)) # 6
print(next(iter_listaaa)) # 3


# Bạn cũng lưu ý, iterator này cũng dính một vấn đề như List, Dict đó chính là chỉnh một, thay đổi hai.
it_1 = iter('kteam')
print(it_1)
it_2 = it_1
print(next(it_2))
print(next(it_1))

# Một số hàm hỗ trợ cho iterable object trong Python

# Một điều lưu ý:  Các hàm này buộc phải lấy các giá trị của iterable để xử lí, do đó nếu bạn đưa vào một iterator. 
# Thì bạn sẽ không sử dụng iterator đó được nữa.

# Hàm tính tổng – sum
# Cú Pháp : sum(iterable,start = 0)
# Công dụng: Trả về tổng các giá trị của iterable và iterable này chỉ chứa các giá trị là số. Còn start chính là giá trị ban đầu.
# Có nghĩa là sẽ cộng từ start lên. Mặc định là 0

print(sum([1,2,3]))
print(sum([1,2,3],10))
print(sum(iter([1,2,3]),10))


# Hàm tìm giá trị lớn nhất – max
# Cú Pháp : max(iterable, *[, default=obj, key=func])
# Công dụng: Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >). Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.

# Dấu * chính là kí hiệu yêu cầu keyword-only argument. Bạn sẽ hiểu thêm khi Kteam giới thiệu parameter trong function.

print(max([1,2,3],default="Dell"))
print(max([],default="dell"))

# Hoặc : max(arg1, arg2, *args, *[, key=func])
# Trong đó:

# *args là packing arguments (bạn sẽ hiểu thêm khi Kteam giới thiệu với bạn packing arguments). 
# Ở đây không có parameter default, vì khi theo cách này, bạn luôn luôn có ít nhất 2 giá trị so sánh

print(max(1,2,3))
print(max(1,2))

# Hàm tìm giá trị nhỏ nhất – min
# Cú pháp:
# min(iterable, *[, default=obj, key=func])

# hoặc

# min(arg1, arg2, *args, *[, key=func])

# Ý nghĩa: giống như hàm max. Khác ở chỗ đây là tìm giá trị nhỏ nhất
print(min([1,2,4]))
print(min([],default="None"))

# Hàm sắp xếp – sorted
# Cú pháp: sorted(iterable, /, *, key=None, reverse=False)
# Công dụng: Giống với phương thức sort của List object.

print(sorted([1,2,3,4,5], reverse=False))
print(sorted([1,2,3,4,5],reverse=True))

