# Dict(Dictionary) cũng là một container như LIST, TUPLE. Có điều khác biệt là những container như List, 
# Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.

# Chắc bạn cũng dùng từ điển tiếng Anh để tra từ vựng rồi nhỉ? Có rất nhiều từ vựng trong đó nhưng mà 
# không từ vựng nào giống nhau. Có chăng chúng chỉ giống nhau về nghĩa? Và đó cũng như Dict(Dictionary)
# hoạt động trong Python

# Một Dict gồm các yếu tố sau:

# *Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
# *Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
# *Các phần tử của Dict phải là một cặp key-value
# *Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
# *Các key buộc phải là một hash object

# Cách Khởi Tạo Dict
# Sử dụng cặp  dấu ngoặc {} và đặt giá  trị bên trong

# Cú Pháp : {<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}
dic = {"key1" : "value1",2 : "hai", (1,2):"One,Two"}
print(dic,"\n")
dic = {} # khởi tạo dict rỗng
print(dic,"\n")
print(type(dic),"\n")

# Sử dụng Dict Comprehension
# Điều kiện để sử dụng dict comprehension là mỗi giá trị khi được duyệt qua phải bao gồm một giá trị 
# tương ứng với key và một giá trị tương ứng với value.

dic = {key : value for key,value in [('Name','Kteam'),('Member',69)]}
print(dic,"\n")

# Sử dụng constructor Dict
# Với dict, ta có 4 cách để khởi tạo một Dict bằng constructor:

# Khởi tạo một Dict rỗng
# Cú Pháp : dict()
dic = dict()
print(dic,"\n")

# Khởi tạo một dict từ một mapping object  
# Cú Pháp : dict(mapping)

# Trong đó:

# Mapping object cũng gần giống so với dict object.

# Một object là Mapping object khi có đủ hai phương thức keys và __getitem__.
# Dict object cũng là một mapping object. Tuy nhiên, không phải mapping object nào cũng là dict object vì dict object không chỉ có hai phương thức keys và __getitem__ và còn nhiều phương thức khác.
# Bạn có thể bỏ qua ví dụ bên dưới hoặc xem để tham khảo vì phần này có thể khá khó hiểu
class Map_class:
    def keys(self):
        return [1,2,3]
    def __getitem__(self,key):
        return key * 2
map_obj = Map_class()
dic = dict(map_obj)
print(dic,"\n")

# Khởi tạo bằng iterable
# Cú Pháp : dict(iterable)

# Trong đó:

# iterable này đặc biệt hơn hơn các iterable mà bạn dùng để khởi tạo List hay Tuple, đó là các phần tử 
# trong iterable phải có 2 value đó chính là cặp key-value.

# Bạn có thể dùng List, Tuple hoặc bất cứ container nào (trừ mapping object) để chứa cặp key-value.
# Ví dụ 1
iter_ = [('name', 'Kteam'), ('member', 69)]
dic = dict(iter_)
print(dic,"\n")
# {'name': 'Kteam', 'member': 69}

# Ví dụ 2
f = [('ab'), ('cd')]
print( dict(f),"\n")
# {'a': 'b', 'c': 'd'}

# Lưu ý: Nếu các bạn muốn khởi tạo dict bằng chuỗi như trên thì bắt buộc độ dài của chuỗi phải là 2. 
# Giá trị đầu sẽ là key, giá trị thứ 2 là value.

# Khởi tạo bằng keyword arguments
# Cú Pháp : dict(<key_1> = <value_1>, <key_2> = <value_2>, ...)
# Khi khởi tạo dict bằng keyword arguments chỉ có thể hoạt động khi các key là tên các biến, 
# còn các value là giá trị của các key tương ứng với nó (các biến có thể được khởi tạo trong cặp ngoặc {}).
name = "spacex"
member = 12312
dic = dict(name = "Kteam", member = 69)
print(dic)
print(name,"\n",member,"\n")

# Sử dụng Phương thức fromkeys

# Cú Pháp : dict.fromkeys(iterable, value)
# Công dụng: Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. 
# Các giá trị này đều sẽ nhận được một giá  trị với mặc định là None
iter_ = ('name', 'number')
dic_none = dict.fromkeys(iter_,"None Nha")
print(dic_none,"\n")

# Lấy value trong Dict bằng key 
# Cú Pháp : Your_dict[key]
dic = {'name': 'Kteam', 'member': 69}
print(dic['name'],"\n")

# Thay đổi nội dung Dict trong Python
# Dict là một unhashable object. Do đó, chắc bạn cũng biết ta có thể thay đổi được nội dung nó hay không.
# Nếu bạn nào nhanh trí, chắc cũng đã biết được cách thay đổi rồi. Tương tự như List thôi!

dic['name'] = 'Tien'
print(dic,"\n")

# Thêm thủ công một phần tử vào dict
# Cách này khá giống với cách bạn thay đổi nội dung của Dict. Khác ở chỗ, bây giờ bạn sẽ sử dụng một
# key chưa hề có trong dict.

dic['class'] = 'CNTT'
print(dic)


# Vấn đề cần lưu tâm khi sử dụng dict
# Các bạn còn nhớ phần “Vấn đề cần lưu tâm khi sử dụng list” chứ ? Đối với dict, ta cũng cần có các
# lưu ý tương tự như vậy. Kteam sẽ đưa ra một vài ví dụ để cho các bạn hiểu. Nếu cần thiết, các bạn có 
# thể xem lại bài “Kiểu dữ liệu list trong Python – Phần 1”.

# Các lỗi dễ xảy ra với list cũng có thể xảy ra với dict

# >>> a = {1: '1', 2: '2', 3: '3'}
# >>> b = a
# >>> a is b
# True
# >>> b[1] = 't'
# >>> a
# {1: 't', 2: '2', 3: '3'}
# >>> b
# {1: 't', 2: '2', 3: '3'}
# >>> a[4] = '4'
# >>> b
# {1: 't', 2: '2', 3: '3', 4: '4'}
# >>> a
# {1: 't', 2: '2', 3: '3', 4: '4'}
# Và tất nhiên, có lỗi thì sẽ có cách sửa chữa

# >>> a = {1: '1', 2: '2', 3: '3'}
# >>> b = a.copy() # Phương thức copy
# >>> b is a
# False
# >>> b
# {1: '1', 2: '2', 3: '3'}
# >>> c = dict(a) # Khởi tạo dict mới
# >>> c is a
# False
# >>> c
# {1: '1', 2: '2', 3: '3'}