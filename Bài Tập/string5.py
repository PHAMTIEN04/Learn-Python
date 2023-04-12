# split()
# Cú Pháp : <Chuỗi>.split(sep = None, maxsplit = -1)
# Công Dụng : Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) bằng cách chia các phần tử bằng kí tự sep.
# Nếu sep mặc định bằng None thì sẽ dùng kí tự khoảng trắng.
# Nếu maxsplit được mặc định bằng -1, Python sẽ không bị giới hạn việc tách, còn không, Python sẽ tách với số lần được cung cấp thông qua maxsplit.
text = "how kteam free education"
sp = text.split(' ')
print("Sau khi sử dụng phương thức split :")
print(sp,"\n")

# rsplit()
# Cú Pháp : <Chuỗi>.rsplit(sep = None, maxsplit = -1)
# Công Dụng : Cũng hoàn toàn như phương thức split, có điều là việc tách từ bên phải sang trái
rsp = text.rsplit(' ',1)
print("Sau khi sử dụng phương thức rsplit :")
print(rsp,"\n")

# partition()
# Cú Pháp : <chuỗi>.partition(sep)
# Công Dụng : Trả về một tuple với 3 phần tử. Các phần tử đó lần lượt là chuỗi trước chuỗi sep, sep và  chuỗi sau sep.
# Lưu Ý : Trong trường hợp không tìm thấy sep trong chuỗi, mặc định trả về giá trị đầu tiên là chuỗi ban đầu và 2 giá trị kế tiếp là 
# chuỗi rỗng.
par = text.partition('y')
print("Sau khi sử dụng phương thức partition :")
print(par,"\n")

# rpartition()
# Cú Pháp : <chuỗi>.rpartition(sep)
# Công Dụng : Cách phân chia giống như phương thức partition nhưng lại chia từ phải qua trái. Và với sep không có trong chuỗi thì sẽ 
# trả về 2 giá trị đầu tiên là chuỗi rỗng và cuối cùng là chuỗi ban đầu.
rpar = text.rpartition('y')
print("Sau khi sử dụng phương thức rpartition :")
print(rpar,"\n")

# count()
# Cú Pháp : <chuỗi>.count(sub, [start, [end]])
# Công Dụng : Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi. Còn start và end là số kĩ thuật slicing
# (lưu ý không hề có bước).
co = text.count('o',0,1)
print("Sau khi sử dụng phương thức count :")
print(co,"\n")

# startswith()
# Cú Pháp : <chuỗi>.startswith(prefix[, start[, end]])
# Công Dụng :Trả về  giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False.
# Lưu ý : Hai yếu tố start, end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.
ssw = text.startswith('how',0,10)
print("Sau khi sử dụng phương thức startswith :")
print(ssw,"\n")

# endswith()
# Cú Pháp : <chuỗi>.endswith(prefix[, start[, end]])
# Công Dụng : Cũng hoàn toàn như phương thức startswith, có điều là việc tách từ bên phải sang trái
esw = text.endswith('n',0,9)
print("Sau khi sử dụng phương thức endswith :")
print(esw,"\n")

# find()
# Cú Pháp : <chuỗi>.find(sub[, start[, end]])
# Công Dụng : Trả về một số nguyên, là vị trí đầu tiên của sub khi dò từ trái sang phải trong chuỗi. Nếu sub không có trong chuỗi, 
# kết quả sẽ là -1. Vẫn như các phương thức khác, start end đại diện cho slicing và ta sẽ tìm trong chuỗi slicing này.
f = text.find('k',0,10)
print("Sau khi sử dụng phương thức find :")
print(f,"\n")

# rfine()
# Cú Pháp : <chuỗi>.find(sub[, start[, end]])
# Công dụng : Tương tự phương thức find nhưng tìm từ phải sang trái
rf = text.rfind('d')
print("Sau khi sử dụng phương thức rfind :")
print(rf,"\n")

# index()
# Cú Pháp : <chuỗi>.index(sub[, start[, end]])
# Công dụng : Tương tự phương thức find. Nhưng khác biệt là sẽ có lỗi ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu
ind = text.index('d')
print("Sau khi sử dụng phương thức index :")
print(ind,"\n")

# rindex()
# Cú Pháp : <chuỗi>.rindex(sub[, start[, end]])
# Công dụng : Tương tự phương thức rindex. Và cũng khác ở điểm là sẽ có ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu
rind = text.rindex('d')
print("Sau khi sử dụng phương thức rindex :")
print(rind,"\n")


# CÁC PHƯƠNG THỨC XÁC THỰC

# islower()
# Cú Pháp : <chuỗi>.islower()
# Công dụng :Trả về True nếu tất cả các kí tự trong chuỗi đều là viết thường. Ngược lại là False
il = text.islower()
print("Sau khi sử dụng phương thức islower :")
print(il,"\n")

# isupper()
# Cú Pháp : <chuỗi>.isupper()
# Công dụng :Trả về True nếu tất cả các kí tự trong chuỗi đều là viết hoa. Ngược lại là False
iu = text.isupper()
print("Sau khi sử dụng phương thức isupper :")
print(iu,"\n")

# istitle()
# Cú Pháp : <chuỗi>.istitle()
# Công Dụng : Trả về True nếu chuỗi đó là một dạng title. Ngược lại là False
it = text.istitle()
print("Sau khi sử dụng phương thức istitle :")
print(it,"\n")

# isidentifier()
# Cú Pháp : <chuỗi>.isidentifier()
# Công Dụng : Giúp xác định xem một chuỗi có phải là một định danh hay không.
# Phương thức isidentifier trả về True khi cả ba điều kiện sau được thỏa mãn:
# + Chuỗi phải được bắt đầu bằng dấu gạch dưới (_) hoặc các kí tự chữ cái
# + Chuỗi không được chứa bất kì khoảng trắng nào
# + Không được chứa các kí tự đặc biệt (_, %, $, _...) ngoại trừ việc kí tự đầu tiên có thể là dấu gạch dưới.
iiden = text.isidentifier()
print("Sau khi sử dụng phương thức isidentifier :")
print(iiden,"\n")

# isdigit()
# Cú pháp : <chuỗi>.isdigit()
# Công dụng : Trả về True nếu tất cả các kí tự trong chuỗi đều là những con số từ 0 đến 9
# Lưu ý: Phương thức này gần giống với isnumeric.
idig = text.isdigit()
print("Sau khi sử dụng phương thức isdigit :")
print(idig,"\n")

# isspace()
# Cú pháp : <chuỗi>.isspace()
# Công dụng: Trả về True nếu tất cả các kí tự trong chuỗi đều là kí tự khoảng trắng
isp = text.isspace()
print("Sau khi sử dụng phương thức isspace :")
print(isp,"\n")

# iskeyword()
# Cú Pháp : import keyword
#         keyword.iskeyword(<chuỗi>)
# Công dụng : Công dụng: Trả về True nếu chuỗi đó tương ứng với một từ khóa.
import keyword # Khai báo thư viện keyword

ik = keyword.iskeyword(text)
print ("Sau khi sử dụng phương thức iskeyword :")
print(ik,"\n")







