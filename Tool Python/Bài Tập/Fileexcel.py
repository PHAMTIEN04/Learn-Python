# sử dụng module openpyxl để đọc/ghi file Excel.
import openpyxl

# Dòng mã này sử dụng lệnh import từ module time. Hàm sleep () trong module time dùng để ngừng thực thi chương trình trong số giây cho trước. 
# Chúng ta có thể sử dụng hàm này trong một số tình huống nhất định, chẳng hạn như khi bạn cần đợi một khoảng thời gian nhất định trước khi tiếp tục thực 
# thi chương trình hoặc giả lập quá trình kéo dài.
from time import sleep



# get_file_excel(filename,paper_sheet,cell_location) được sử dụng để đọc các giá trị ở ô trong file Excel. 
# Hàm này nhận vào 3 tham số: tên file Excel (filename), tên sheet trong file (paper_sheet) và vị trí ô cần đọc (cell_location). 
# Nó trả về giá trị của ô tương ứng.
def get_file_excel(filename,paper_sheet,cell_location) :
    wb = openpyxl.load_workbook(filename)
    sheet = wb[paper_sheet]
    wb.close()
    return sheet[cell_location].value


# update_file_execl(filename,paper_sheet,cell_name,value) được sử dụng để cập nhật giá trị vào các ô trong file Exell. 
# Hàm này nhận vào 4 tham số: tên file Excel (filename), tên sheet trong file (paper_sheet), 
# vị trí ô cần cập nhật (cell_name) và giá trị cần ghi vào ô (value).
def update_file_execl(filename,paper_sheet,cell_name,value):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[paper_sheet]
    sheet[cell_name].value = value
    wb.close()
    wb.save(filename)
    
    
    
filename = "Fileexcel.xlsx"
paper_sheet = "Sheet1"
col_location_user = "F"
col_location_pass = "G"

for i_row in range(7,28) : # sử dụng một vòng lặp để duyệt qua các dòng trong file excel từ số thứ tự 7 đến 27. 
    
    # trong mỗi vòng lặp, nó sử dụng biến i_row để xác định vị trí của các ô chứa tài khoản và mật khẩu
    cell_name_acc = "%s%s"%(col_location_user,i_row)
    cell_name_pass = "%s%s"%(col_location_pass,i_row)
    
    # lấy giá trị của cặp tài khoản và mật khẩu từ file excel bằng cách gọi hàm get_file_excel và in ra trên màn hình
    account = get_file_excel(filename,paper_sheet,cell_name_acc)
    password = get_file_excel(filename,paper_sheet,cell_name_pass)
    print("Account  :",account)
    print("Password :",password)
   
    # Sau đó, chương trình sẽ ngủ 0.1 giây (bởi vì sleep(0.1) được gọi) trước khi tiếp tục vòng lặp cho đến khi tất cả các cặp tài khoản và mật khẩu được xử lý.
    sleep(0.1)
    
    


