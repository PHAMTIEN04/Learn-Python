#"gspread" là một thư viện Python để tương tác với Google Sheets thông qua Google Sheets API. Nó cho phép người dùng đọc, 
# ghi và cập nhật dữ liệu trên các bảng tính Google thông qua mã Python của mình.
import gspread 
# Thư viện Python để làm việc với các tệp Excel (.xlsx), cho phép đọc, ghi và chỉnh sửa các tệp này trong Python.
import openpyxl
# Thư viện Python để phân tích cú pháp HTML và XML. Nó cho phép người dùng tìm kiếm, trích xuất và xử lý dữ liệu từ các trang web và tệp HTML/XML.
import bs4
# Thư viện Python để thực hiện các yêu cầu HTTP trong Python. Nó cho phép người dùng gửi yêu cầu đến các trang web và nhận lại phản hồi.
import requests
# Thư viện Python cho các biểu thức chính quy. Nó cho phép người dùng tìm kiếm và thay thế chuỗi dựa trên các quy tắc được định nghĩa sẵn.
import re
# Thư viện Python để tương tác với hệ điều hành, cho phép người dùng thực hiện các hoạt động như tạo, đổi tên, xóa và di chuyển các tệp và thư mục.
import os
from time import sleep

os.chdir(r"C:\Learn Python\Tool Python\Project\Project3 UpdatePriceCoinGGS")

# filename: Tên tệp JSON chứa thông tin xác thực để truy cập vào Google Sheets API.
# key: Khóa của bảng tính Google Sheets cần được cập nhật.
# col_row: Vị trí ô cần được cập nhật, được đưa vào dưới dạng chuỗi, ví dụ "A1" hoặc "C4".
# value: Giá trị mới để cập nhật cho ô tương ứng.
# Trong hàm, thư viện gspread được sử dụng để xác thực truy cập vào tài khoản Google Sheets của người dùng thông qua tệp filename. 
# Sau đó, bảng tính được mở bằng khóa key và ô tại vị trí col_row trên trang tính sheet1 được cập nhật với giá trị mới value bằng phương thức update của worksheet.
def updatepricecoin(filename,key,col_row,value) :
    gs = gspread.service_account(filename) 
    sht = gs.open_by_key(key)
    sht.sheet1.update(col_row,value)

i = 0
    
while True: #Vòng lặp vô hạn
     # Lấy mã nguồn
    url = 'https://coinmarketcap.com/'
    response = requests.get(url=url)
    html_code = response.text   
    filename = 'codegs.html'
    # Cho mã nguồn vào file 
    with open(file=filename,mode='w',encoding="utf8") as file_open:
        file_open.write(html_code)
        # Tách giá trị của mã nguồn cần tach
    soup = bs4.BeautifulSoup(html_code, 'html.parser')
    eles = soup.select('span')
            # Lấy giá trị vừa tách xong viết nó vào file mới
    with open(file='Checkgs.txt', mode='w', encoding='utf8') as filename_check:
        for elem in eles:
            text = elem.get_text()
            filename_check.write(text + ' ')  
    filename_text = 'Checkgs.txt'
    # Đọc giá tri của File 
    with open(file=filename_text, mode='r', encoding='utf8') as file_text:
        check_regex = file_text.read()
        # print(check_regex)
        # Regex điều kiện
    regex_btc = re.compile(r'                    (.*?) ')
    regex_hb = re.compile(r'Huobi Token HT (.*?)     ')
    regex_ape = re.compile(r'ApeCoin APE (.*?)     ')
    regex_apt = re.compile(r'Aptos APT (.*?)     ')
    regex_agix = re.compile(r'SingularityNET AGIX (.*?)     ')
            # Regex tìm kiếm giá trị đó cùng điều kiện 
    kq_btc = regex_btc.search(check_regex)
    kq_hb = regex_hb.search(check_regex)
    kq_ape = regex_ape.search(check_regex)
    kq_apt = regex_apt.search(check_regex)
    kq_agix = regex_agix.search(check_regex)
            # Lấy giá trị của Regex vừa tìm kiếm được
    text_btc = kq_btc.group(1)
    text_hb = kq_hb.group(1)
    text_ape = kq_ape.group(1)
    text_apt = kq_apt.group(1)
    text_agix = kq_agix.group(1)
    # Tên tệp JSON chứa thông tin xác thực để truy cập vào Google Sheets API.
    filename = 'cre.json'
    #  Khóa của bảng tính Google Sheets cần được cập nhật.
    key = '14dCyt0sBZgm171zAzsPlhnrknGt24jbxkxzVKQXBY6o'
    # Update tên coin
    updatepricecoin(filename=filename,key=key,col_row="A1",value="Bitcoin")
    updatepricecoin(filename=filename,key=key,col_row="A2",value="Houbi")
    updatepricecoin(filename=filename,key=key,col_row="A3",value="Ape")
    updatepricecoin(filename=filename,key=key,col_row="A4",value="Apt")
    updatepricecoin(filename=filename,key=key,col_row="A5",value="Agix")
    # Update giá trị coin
    updatepricecoin(filename=filename,key=key,col_row="B1",value=text_btc)
    updatepricecoin(filename=filename,key=key,col_row="B2",value=text_hb)
    updatepricecoin(filename=filename,key=key,col_row="B3",value=text_ape)
    updatepricecoin(filename=filename,key=key,col_row="B4",value=text_apt)
    updatepricecoin(filename=filename,key=key,col_row="B5",value=text_agix)
    i = i + 1
    print("Đang cập nhật:",i)
    sleep(60)
    
    
    