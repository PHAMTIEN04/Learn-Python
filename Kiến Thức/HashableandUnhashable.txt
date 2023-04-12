
# id()
# Cú Pháp : id(<giá trị>)
# Công Dụng : Theo định nghĩa về hàm id trong tài liệu của Python thì hàm này sẽ trả về một số nguyên (int hoặc longint).
# Giá trị này là một giá trị duy nhất và là hằng số không thay đổi suốt chương trình.
# Trong chi tiết bổ sung của CPython có nói giá trị trả về của hàm id là địa chỉ của giá trị (đối tượng) đó trong bộ nhớ.
# Cao siêu là thế, nhưng bạn hoàn toàn có thể nghĩ đơn giản, con số trả về đó như cái số nhà của bạn. Bạn ở đâu, thì số nhà của bạn cũng sẽ tương ứng.
x = [1,2,3]
y = [1,2,3]
z = x
print(id(x)) # 139922931551872
print(id(y)) # 139922931553344 (khác x)
print(id(z)) # 139922931551872 (giống x)

# Toán Tử Là Một Phương Thức 
# Mọi thứ xoay quanh Python toàn là hướng đối tượng. Cả các toán tử cũng thế!
n = 69
print(n + 1)
# trả về 70
print (n)
# trả về 69
print (n.__add__(1)) # tương tự khi bạn n + 1
# trả về 70
print (n)
# trả về 69	
print (n.__sub__(9)) # tương tự n - 9
# trả về 60
print (n.__mul__(2)) # tương tự n * 2
# trả về 138
print (n.__radd__(1)) # tương tự 1 + n
# trả về 70
print (n.__rsub__(9)) # tương tự 9 - n
# trả về -60
print (n.__neg__()) # tương tự -n
# trả về -69

# - Hash :
#  (bộ nhớ chỉ đủ cho 'b' tồn tại, khi thay đổi ndung chỉ có cách tìm địa chỉ mới để xây 1 căn nhà bự hơn)
#    1. (b+= 1) y chang (b = b +1) -- đều 'khởi tạo' biến 'b' MỚI và KHÁC HOÀN TOÀN
#    2. không có _iadd_
#  (phương thức) -


# - Unhash:
#  (bộ nhớ thừa cho 'n' , khi sửa ndung thì ko cần tìm địa chỉ mới --> id() giữ nguyên)
#    1. (n+=1) khác (n = n+1)
#   --- ( 1 bên sửa ndung) và ( 1 bên 'gán' - 'khởi tạo' biến 'n' MỚI và KHÁC HOÀN TOÀN)
#    2. có _iadd_ chính là (n+=1) -- làm thay đổi nội dung

# - Với 'n.__add__(2)' ta hiểu đó chỉ là (toán tử) '+' khi đứng một mình thì k có nghĩa gì hết.
#       --> n + 2
# - Còn 'n.__iadd__(2)' (phương thức chỉ  có ở Unhash) 
#       ---> n+= 2 ( thay đổi ndung mà ko đổi id() )

# Ví dụ về Hashable là str :

hash_a = "How"
print(id(hash_a))
hash_a += "Kteam"
print(id(hash_a))

# Ví dụ về Unhashable là list :

hash_u = [1,2,3]
print(id(hash_u))
hash_u = hash_u + [4]
print(id(hash_u))
