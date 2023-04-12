# Toán tử +, -, *, / 
# Toán tử so sánh ==, !=, >, <, >=, <=
kieu_int = 4 #kieu intergers
kieu_float = 5.3 #kieu float
kieu_str = "aaa" #kieu str
# type : Dùng để in ra Kiểu Dữ Liệu 
print(type(kieu_int))
print(type(kieu_float))
print(type(kieu_str))

# Lấy toàn bộ nội dung thư viện decimal
from decimal import*
# lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal
getcontext().prec = 30

print(Decimal(10)/Decimal(3))

# Hàm số phức complex
c = complex(2,5)
print(c)
# Lấy số thực 
print(c.real)
# lấy số ảo
print(c.imag)
#lấy toàn bộ nội dung thư viện fractions
from fractions import*
#Fraction(Tử,Mẫu) : hàm phân số 
frac1 = Fraction(6,9)
frac2 = Fraction(5,9)
frac3 = (frac1 + frac2) 
print(frac3)

#lấy toàn bộ nội dung thư viện math
import math
#muốn sử dụng 1 hàm nào đó của 1 thư viện ta dùng cú pháp
#<tên thư viện>.<tên hàm>
print("Ước chung lớn nhất :",end='')
print(math.gcd(3,6))