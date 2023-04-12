
# count()
# Cú Pháp : <List>.count(sub, [start, [end]])
# Công dụng : Giống với phương thức count của kiểu dữ liệu chuỗi.
# Lưu ý : + Trả về một số nguyên, chính là số lần xuất hiện của sub trong List.
#         + Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).
text = [1,2,2,4,8,9,7]
print("List Ban Đầu : ",text,"\n")
co = text.count(2)
print("Sau khi sử dụng phương thức count trong List : ",end='')
print(co,"\n")

# index()
# Cú Pháp : <List>.index(sub[, start[, end]])
# Công Dụng : Tương tự phương thức index của kiểu dữ liệu chuỗi 
ind = text.index(1)
print("Sau khi sử dụng phương thức index trong List : ",end='')
print(ind,"\n")

# copy()
# Cú Pháp : <List>.copy()
# Công dụng : Trả về một List tương tự List[:]
# Lưu Ý : Chỉ sao chép chứ không trỏ cùng 1 địa chỉ
cop = text.copy()
cop[0] = "HOW"
print("Sau khi sử dụng phương thức copy trong List : ")
print(cop)
print(text,"\n")

# clear()
# Cú Pháp : <List>.clear()
# Công dụng : Xóa mọi phần tử có trong List. 
# Lưu ý: Các phiên bản Python 2.X hoặc dưới Python 3.2 sẽ không có phương thức này
# Nó sẽ xóa mọi phần tử trong List text1 được chọn còn nếu có biến gán thì nó sẽ trả về none bởi vì biến gán đó gán trị không phải List text1
# Ngược lại nếu biến gán mà = List text1 thì khi sử dụng Clear sẽ xóa cả 2 và trả về [] ( rỗng )
text1 = [1,2,3,4,5]
cle = text1.clear()
print("Sau khi sử dụng phương thức clear trong List : ",)
print(text1)
print(cle,"\n")

# CÁC PHƯƠNG THÚC CẬP NHẬT
# Đặc biệt phương thức này không gán biến được nếu gán biến thì giá trị của biến đó sẽ là None

# append()
# Cú Pháp : <List>.append(x)
# Công dụng: Thêm phần tử x vào cuối List
# Chú ý: Đừng bao giờ append một list vào chính nó.
# Khi ta append một list vào chính nó, thì trên thực tế, nó sẽ tạo ra một vòng lặp vô tận. Trong ví dụ trên, khi ta append a vào list a, thì nó sẽ truy xuất giá trị của a để có thể 
# append. Nhưng vì giá trị của a đang được thay đổi, nên nó sẽ lại append trước khi truy xuất. Điều này sẽ lặp lại mãi mãi vì giá trị a sẽ luôn luôn được thay đổi. 
# Kết quả [1, 2, [...]] chính là đại diện cho sự lặp vô tận đó.


text.append(4)
print("Sau khi sử dụng phương thức append trong List : ",end='')
print(text,"\n")

# extend()
# Cú Pháp : <List>.extend(iterable)
# Công dụng: Thêm từng phần tử một của iterable vào cuối List.
text.extend([4,5,6])
print("Sau khi sử dụng phương thức extend trong List : ",end='')
print(text,"\n")

# insert()
# Cú Pháp : <List>.insert (i, x)
# Công dụng: Thêm phần x vào vị trí i ở trong List.
# Lưu ý :Nếu vị trí i lại lớn hơn hoặc bằng số phần tử ở trong List thì kết quả sẽ tương tự như phương thức append.
# Nếu vị trí i –1 (đang xét indexing âm) không có trong List, mặc định, phần tử x sẽ được thêm vào đầu List
# Chú ý: Cũng giống như phương thức append, Kteam khuyên bạn đừng bao giờ insert một list vào chính nó, bất kể ở vị trí nào.
text.insert(1,10)
print("Sau khi sử dụng phương thức insert trong List : ",end='')
print(text,"\n")

# pop()
# Cú Pháp : <List>.pop([i])
# Công dụng: Bỏ đi phần tử thứ i trong List và trả về giá trị đó. Nếu vị trí i không được cung cấp, 
# phương thức này sẽ tự bỏ đi phần tử cuối cùng của List và trả về giá trị đó.
text.pop(1)
print("Sau khi sử dụng phương thức pop trong List : ",end='')
print(text,"\n")

# remove()
# Cú Pháp : <List>.remove(x)
# Công dụng :  Bỏ đi phần tử đầu tiên trong List có giá trị x. Nếu trong List không có giá trị x sẽ có lỗi được thông báo
text.remove(1)
print("Sau khi sử dụng phương thức remove trong List : ",end='')
print(text,"\n")

# CÁC PHƯƠNG THỨC XỬ LÍ
# Đặc biệt phương thức này không gán biến được nếu gán biến thì giá trị của biến đó sẽ là None

# reverse()
# Cú Pháp : <List>.reverse()
# Công dụng: Đảo ngược các phần tử ở trong List.
text.reverse()
print("Sau khi sử dụng phương thức reverse trong List : ",end='')
print(text,"\n")

# sort()
# Cú Pháp : <List>.sort(key=None, reverse=False)
# Công dụng:  Sắp xếp các phần tử từ bé đến lớn bằng cách so sánh trực tiếp.
# Trong đó:
# Nếu reverse là False (false là giá trị mặc định), list sẽ được sắp xếp từ bé đến lớn (các phần tử nhỏ hơn sẽ đứng trước), và ngược lại, nếu reverse là True, list sẽ được sắp xếp từ lớn đến bé.
# Tham số key mặc định là None (tức là sẽ sắp xếp một cách mặc định). Còn nếu key được chỉ định, thì các phần tử được sắp xếp theo cái “quy ước” của key.
print("CÁC CÁCH XỬ LÍ PHƯƠNG THỨC SORT TRONG LIST :")
# Ví dụ 1: sắp xếp các list (key = None)
text.sort()
print(text,"\n")

# Ghi nhớ rằng, các phần tử phải có thể so sánh với nhau. Trường hợp dưới đây bạn không thể so sánh chuỗi với số được, do đó sẽ có lỗi hiện lên.

# Chúng ta sẽ nói đến từ khóa reverse. Từ khóa này bạn chỉ có thể cho 2 giá trị, một là True, hai là False.
# Nếu là False, các phần tử được sắp xếp từ bé đến lớn, còn ngược lại là từ lớn đến bé.
text.sort(reverse=True)
print(text,"\n")

# Ví dụ 2: sắp xếp các list (có tham số key được truyền vào)
text_sort =  ['This', 'is', 'How', 'Kteam']
text_sort.sort(key=len)
print(text_sort,"\n")
#  list text_sort, chương trình sẽ sắp xếp dựa trên việc so sánh độ dài của các chuỗi (vì key = len, tức là lấy độ dài). Kết quả của text_sort sau khi sort là một list có các chuỗi với độ dài 
# tăng dần.

# Ví dụ dưới đây là một cách sắp xếp một list với cả chuỗi và số, dựa trên việc chuyển toàn bộ các số sang kiểu chuỗi và so sánh.
text_sort_str = ['a', 1, 'b', 2, 2, 'b']
text_sort_str.sort(key=str)
print(text_sort_str,"\n")

#BÀI TẬP
#1. Chuyện gì xảy ra khi ta dùng phương thức pop lên một List rỗng
text_none = list()
text_none.pop(1)
print(text_none)
# = > Khi ta dùng phương thức Pop lên một list rỗng nó sẽ báo lỗi vì không tìm thấy vị trí thứ i

#2. Ta có thể sắp xếp được List dưới đây bằng phương thức sort hay không?
text_sort_bt = [[1, 2], ['a', 'd']]
text_sort_bt.sort()
print(text_sort_bt)
# Không. Vì khi đó, ta phải so sánh hai List [1, 2] và ['abc', 'def']. Mà khi so sánh hai List này một cách trực tiếp. Python sẽ phải so sánh từng phần tử của mỗi hai List đó với nhau.
# Nhưng một bên là số, một bên là chuỗi, nên việc so sánh trực tiếp là không được.



