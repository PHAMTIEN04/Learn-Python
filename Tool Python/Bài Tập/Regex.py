# import module re
import re 

print("nghiassh")
# Hàm compile() được sử dụng để biên dịch một biểu thức chính quy vào một đối tượng pattern để sử dụng cho các mục đích tìm kiếm chuỗi về sau. 
# Nội dung biểu thức chính quy này là r'anh (.*?) dep', có ý nghĩa tìm kiếm chuỗi con bắt đầu bằng từ "anh" và kết thúc bằng từ "dep" với bất kỳ 
# chuỗi nào ở giữa. Ký tự .*? được sử dụng để đại diện cho bất kỳ chuỗi nào cũng được tính đến.
# . là lấy mọi ký tự 
# * lặp lại từ đến nhiều nhất có thể (noon-greedy) 
# "?" : Điều kiện chỉ gặp dep là dừng
regexl = re.compile(r'anh (.*?) dep')
print(type(regexl))
chuoidemo = "anh nghiassh dep trai dep"
#  hàm findall() từ regexl trong module re để tìm kiếm tất cả các chuỗi con phù hợp với mẫu đã định nghĩa trong biểu thức chính qui (pattern) ở 
# regexl. Kết quả được gán vào biến kq, kết quả trả về là danh sách (list) chứa các chuỗi con phù hợp với biểu thức điều kiện đã định sẵn.
kq = regexl.findall(chuoidemo)
print(kq)


# Câu lệnh regexl1.search(chuoidemo) sử dụng hàm search của đối tượng biểu thức chính quy để tìm kiếm chuỗi con đầu tiên trong chuỗi "chuoidemo" 
# phù hợp với mẫu biểu thức chính quy đã chỉ định và trả về một đối tượng MatchObject. Trong ví dụ này, đối tượng MatchObject chứa chuỗi 
# "anh nghiassh dep trai".

# Cuối cùng, .group() được gọi trên đối tượng MatchObject để trả về chuỗi con đã khớp. Kết quả trả về là "anh nghiassh dep trai".
regexl1 = re.compile(r'anh (.*?) dep')
kq1 = regexl1.search(chuoidemo)
print(kq1.group(1))