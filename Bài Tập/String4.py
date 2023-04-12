a = 'a'
# ASCII
# Hàm ord() sẽ lấy giá trị Int của Char
# Hàm chr() sẽ lấy giá trị Char của Int
b =  ord(a)- 32
chuyen_doi = chr(b)
print(chuyen_doi)
# import time
text = "how kteam - free education"
# capitalize() 
# Cú Pháp : <chuỗi>.capitalize() 
# Cộng Dụng : Trả về một chuỗi với kí tự đầu viết hoa và viết thường tất cả những kí tự còn lại
c = text.capitalize()
print(text)
# time.sleep(1)
# print(". " , end='')
# time.sleep(1)
# print(". " , end='')
# time.sleep(1)
# print(". " , end='')
# time.sleep(1)
# print(". " )
print("Sau Khi chuyển đổi bằng capitalize :")
print(c)

# upper()
# Cú Pháp : <chuỗi>.upper()
# Công dụng : Trả về một chuỗi với tất cả kí tự được chuyển thành kí tự viết hoa
u = text.upper()
print("Sau Khi chuyển đổi bằng upper:")
print(u)

# lower()
# Cú Pháp : <chuỗi>.lower()
# Công dụng : Trả về một chuỗi với tất cả kí tự được chuyển thành kí tự thường
l = text.lower()
print("Sau Khi chuyển đổi bằng lower:")
print(l)

# swapcase()
# Cú Pháp : <chuỗi>.swapcase
# Công dụng : Trả về một chuỗi với các kí tự viết hoa được chuyển thành viết thường, các kí tự viết thường được chuyển thành viết hoa
s = text.swapcase()
print("Sau Khi chuyển đổi bằng swapcase:")
print(s)

# title()
# Cú Pháp : <chuỗi>.title()
# Công dụng : Trả về một chuỗi định dạng là tiêu đề, có nghĩa là các từ  sẽ được viết hoa chữ cái đầu tiên, còn lại viết thường
t = text.title()
print("Sau Khi chuyển đổi bằng title :")
print(t)

# center()
# Cú Pháp : <Chuỗi>.center(width,[fillchar])
# Công dụng : Trả về mỗi chuỗi được căn giữa với chiều rộng width
# Lưu Ý : + Nếu fillchar là None(không được nhập vào) thì sẽ dùng kí tự khoảng trắng để căn, không thì sẽ căn bằng kí tự fill char
#         + Một điều nữa là kí tự fillchar là một chuỗi có độ dài là 1
ce = text.center(100,'-')
print("Sau Khi chuyển đổi bằng center :")
print(ce)

# rjust()
# Cú Pháp : <Chuỗi>.rjust(width,[fillchar])
# Công dụng : Cách hoạt động như phương thức center, có điều là căn lề phải
rj = text.rjust(100,"+")
print("Sau Khi chuyển đổi bằng rjust :")
print(rj)

# ljust()
# Cú Pháp : <Chuỗi>.ljust(width, [fillchar])
# Công dụng : Cách hoạt động như phương thức center, nhưng căn lề trái
lj = text.ljust(100,"*")
print("Sau Khi chuyển đổi bằng ljust :")
print(lj,"\n")

# Các Phương Thức Xử Lí

# encode()
# Cú Pháp : <Chuỗi>.encode(encoding = 'utf-8', errors='strict')
# Công dụng : Đây là phương thức dùng để encode một chuỗi với phương mã hóa mặc định là utf-8.
# Còn về errors mặc định sẽ là strict có nghĩa là sẽ có thông báo lỗi hiện lên nếu có vấn đề xuất hiện trong quá trình encode chuỗi.
# Một số giá trị ngoài strict là ignore, replace, xmlcharrefreplace
text1 = "Ô hay cái gì thế"
en = text1.encode()
print("Sau khi xử dụng phương thức xử lí encode:")
print(en)
# Đặt vấn đề : Nếu ta muốn làm ngược lại (tức là giải mã một chuỗi đã được encode) thì làm như thế nào ?
# Đối với trường hợp này, sử dụng phương thức giải mã (phương thức decode
# decode()
# Cú Pháp : <Chuỗi(đã mã hóa)>.decode(encoding ='utf-8', errors = 'strict')
# Công dụng : dùng để giải mã các kí đã được mã bởi phương thức encode
en1 = en.decode()
print("Sau khi giải mã:")
print(en1)

# join()
# Cú Pháp : <Kí tự nối>.join(<iterable>)
# Công dụng : Trả về một chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối. Một iterable có thể là một 
# tuple, list,... hoặc là một iterator.
# Lưu Ý : Các phần tử trong iterable buộc phải thuộc lớp str
jo = text.join(('1','2','3'))
print("Sau khi sử dụng phương thức join")
print(jo)

# replace()
# Cú Pháp : <Chuỗi>.replace(old, new, [count])
# Công dụng : Trả về mỗi chuỗi với các old nằm trong chuỗi ban đầu được thay thế bằng chuỗi new. Nếu count
# khác None (có nghĩa là cho thêm count) thì ta sẽ thay thế old bằng new với lượng count từ trái sang phải
# Lưu ý : Nếu chuỗi old không nằm trong chuỗi ban đầu hoặc count là 0 thì sẽ trả về một chuỗi giống với chuỗi ban đầu
re = text.replace("e","Tiến",1)
print("Sau khi sử dụng phương thức replace")
print(re)

# strip()
# Cú Pháp : <Chuỗi>.strip([chars])
# Công dụng : Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi các kí tự chars. Nếu chars bị bỏ trống thì 
# ta mặc định các kí tự bỏ đi là dấu khoảng trắng và các escape sequence. Một số escape sequence ngoại lệ như \a sẽ được endcode utf-8. 
# Tuy vậy, không có ảnh hưởng gì tới nội dung
text2 = 'ttttiến Đẹp Như titttt'
st = text2.strip('t')
print("Sau kho sử dụng phương thức strip")
print(st)

# rstrip()
# Cú Pháp : <Chuỗi>.rstrip()
# Công dụng : Cách hoạt động hoàn toàn như phương thức strip, nhưng khác là chỉ bỏ đi phần đuôi(từ phải sang trái)
rst = text2.rstrip('t')
print("Sau kho sử dụng phương thức rstrip")
print(rst)

# lstrip()
# Cú Pháp : <Chuỗi>.lstrip()
# Công dụng : Cách hoạt động hoàn toàn như phương thức strip, nhưng khác là chỉ bỏ đi phần đầu(từ trái sang phải)
lst = text2.lstrip('t')
print("Sau kho sử dụng phương thức lstrip")
print(lst)

# removeprefix()
# Cú Pháp : <Chuỗi>.removeprefix([prefix])
# Công dụng : Trả về một chuỗi mới, chính là chuỗi ban đầu đã được bỏ đi [prefix]
# Lưu ý : Nếu [prefix] không xuất hiện ở phần đầu của chuỗi, phương thức removeprefix trả về chính chuỗi đó
removepe = text2.removeprefix('ttt')
print("Sau khi sử dụng phương thức removeprefix :")
print(removepe)

# removesuffix()
# Cú Pháp : <chuỗi>.removesuffix([suffix])
# Công dụng : Công dụng: tương tự như removeprefix, nhưng nó sẽ xóa ở cuối chuỗi.
removesu = text2.removesuffix('ttt')
print("Sau khi sử dụng phương thức removesuffix")
print(removesu)