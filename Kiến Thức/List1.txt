# Giới hạn bởi cặp ngược vuông []
# Các phần tử của list cách nhau bởi dấu ,
# List có khả năng chứa mọi giá trị đối tượng của Python. Và bao gồm chính nó

# list rỗng
list_r = []
print(list_r,"\n")
# List Comprehension
# Khởi tạo 1 list comprehension : <biến> for biến in range(giá trị)
# Vòng lặp chạy từ i mặc định là 0 cho tới giá trị được đặt trong range - 1
list_com = [i for i  in range(30)] 
print(list_com,"\n")

# range(start,end-1)
# start như là thay thế giá trị bắt đầu cho biến i
list_com1 = [[i+2] for i in range(1,4)]
print(list_com1,"\n")

# constructor List
# Cú Pháp : list (iterable)

# Nó như 1 vòng lặp tách từng phần tử ra rồi gán vào list rồi cách nhau bởi dấu ,
list_cons = list('122312312')
print(list_cons,"\n")

# Toán tử +
# Nối hai list lại với nhau
plus = [1,2]
plus += ['one','two']
print(plus,"\n")

# Toán tử *
# Nhân list lên tương tự string
mul = list('Tien') * 2
print(mul,"\n")

# Toán tử in
# Tương tự String nếu như giá trị đó nằm trong list thì sẽ trả về True ngược lại thì False
text = list('kteam')
i = 'c' in text
print(i,"\n")

# CÁC TOÁN TỬ SO SÁNH
# Cú Pháp : A <toán tử so sánh> B (A và B là 2 list)
# Trong Python, cách so sánh 2 list cũng giống như cách so sánh 2 chuỗi.
# Hiểu một cách đơn giản, kết quả của các toán tử so sánh (trên 2 list) sẽ dựa trên việc so sánh 2 list đó. Kết quả trả về sẽ là True hoặc False.
# Khi so sánh 2 list, chương trình sẽ lần lượt so sánh các phần tử có cùng vị trí trong 2 list. Nếu xuất hiện 2 giá trị khác nhau, thì kết quả của phép so sánh sẽ là kết quả khi so sánh 2 giá trị đó.
# Khi so sánh đến hết một trong 2 list nhưng vẫn không có giá trị khác biệt, chương trình sẽ so sánh độ dài của 2 list và trả về kết quả tương ứng.

# A == B
A = [1,2,3]
B = [1,2,3]
equal = A == B
print(equal,"\n")

# C > D
# ACSII giá trị từng phần tử trong list C Nhỏ Hơn List D
C = ['b', 'c', 'd']
D = ['x', 'y', 'z']
bigger = C > D
print(bigger,"\n")

# E < F
E = ['a']
F = ['b']
smaller = E < F
print(smaller,"\n")

# Indexing và Cắt LIST trong Python
text_cut = [1, 2, 'a', 'b', [3, 4]]
print(text_cut[1:3])
print(text_cut[::-1],"\n")

# Thay đổi nội dung List trong Python
text1 = [1, 'two', 3]
text1[1] = 2
print(text1,"\n")


# Lưu Ý Khi Sử dụng List Không được phép gán List này qua List kia nếu không có chủ đích
# >>> another_lst[1]
# 2
# >>> another_lst[1] = 'Two'
# >>> another_lst
# [1, 'Two', 3]
# >>> lst
# [1, 'Two', 3]
# Chỉnh một, nhưng đổi tới hai. Lí do là vì khi bạn gán giá trị List trực tiếp như thế, bạn đang đưa hai List đó trỏ cùng vào một nơi. Nói cách khác, 
# cùng một giá trị list, nhưng lại có đến hai cái tên (có thể có nhiều hơn 2 tùy vào cách ta gán biến).
# Hãy tưởng tượng Tèo có 50 nghìn. Sau đó bạn sử dụng phép thuật của mình gán số tiền cô gấu của Tèo bằng số tiền của Tèo. Khi đó, cô gấu dễ thương của 
# Tèo không tự nhiên mà có 50 nghìn, mà thay vào đó, bạn đã gián tiếp cho phép gấu của Tèo sử dụng số tiền của Tèo nhịn ăn mì tôm bấy lâu nay. Và vào một ngày trơi mưa không rơi, cô ấy chạy đi mua một gói Snack mất 5 nghìn và sử dụng số tiền 50 nghìn bạn vừa mới gán cho cô ấy. Hậu quả là Tèo về thấy mất đâu 5 nghìn.
# Do đó, trước khi gán, bạn phải copy giá trị của List
# Ta có thể chứng thực điều đó bằng cách sử dụng toán tử is.

# Toán tử is 
# Cú Pháp : A is B 
# Công Dụng : Kiểm tra xem hai biến A và B có cùng trỏ đến một đối tượng hay không. Nếu một trong hai biến được gán giá trị bằng biến còn lại, 
# thì kết quả trả về là True.

# Để hiểu rõ hơn về toán tử is, cũng như là lỗi dễ mắc phải khi gán giá trị của các list cho nhau, ta cùng xem xét các ví dụ sau:
a_is = [1, 2, 3]
b_is = [1, 2, 3]
check_is = a_is is b_is 
# Vì a và b trỏ đến 2 giá trị khác nhau, nên việc thay đổi giá trị bên trong của một biến không tác động đến biến còn lại
print(check_is,"\n") #Trả Về False 
c_is = [1, 2, 3]
d_is = c_is
check1_is = c_is is d_is
# Vì a và b trỏ đến cùng một giá trị list, nên việc thay đổi giá trị bên trong của một biến cũng sẽ “kéo theo” sự thay đổi của biến còn lại.
print(check1_is,"\n") # Trả về True

# ĐỌC THÊM LƯU Ý VỀ TOÁN TỬ IS TẠI : https://howkteam.vn/course/kieu-du-lieu-chuoi-trong-python--phan-4/kieu-du-lieu-list-trong-python--phan-1-1548


a = [1,2,5,"Kteam"]
print(a,"\n")

b = [[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]] ,[[[13,14,15],[16,17,18]]]]
print(b,"\n")
t = int(input("Input t :"))
x = int(input("Input x :"))
y = int(input("Input y :"))
z = int(input("Input z :"))
print("Position (Vị Trí) t =",t,"x =",x,"y =",y,"z =",z)
print("The value (Giá Trị) of a list : ",b[t][x][y][z])

