xau = str(input())

location_A = xau.find('A')
location_Z = xau.rfind('Z')

len_max = location_Z - location_A + 1
print(len_max)

# Trong đoạn mã trên, find() và rfind() là hai phương thức có sẵn trong Python cho phép tìm kiếm vị trí đầu tiên và vị trí cuối cùng của một chuỗi con trong 
# chuỗi đầu vào. Nếu ký tự 'A' không tồn tại trong chuỗi đầu vào hoặc ký tự 'Z' không tồn tại trong chuỗi đầu vào hoặc vị trí của ký tự 'A' đứng sau vị trí của 
# ký tự 'Z', chương trình sẽ in ra số 0. Nếu không, chương trình sẽ tính độ dài của đoạn con của chuỗi bằng cách lấy hiệu của vị trí ký tự 'Z' cuối cùng và vị trí
# ký tự 'A' đầu tiên và in ra kết quả. Độ phức tạp thời gian của chương trình này là O(n), với n là độ dài của chuỗi đầu vào, do chỉ có hai 
# phương thức find() và rfind() được sử dụng.