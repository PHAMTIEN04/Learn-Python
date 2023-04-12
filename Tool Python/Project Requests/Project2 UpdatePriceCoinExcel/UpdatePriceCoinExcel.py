import openpyxl
import bs4
import requests
import re
import os
from time import sleep
from colorama import Fore,Style

os.chdir(r"C:\Learn Python\Tool Python\Project\Project2 UpdatePriceCoinExcel")
while True: #Vòng lặp vô hạn
     # Lấy mã nguồn
    url = 'https://coinmarketcap.com/'
    response = requests.get(url=url)
    html_code = response.text   
    filename = 'codeex.html'
    # Cho mã nguồn vào file 
    with open(file=filename,mode='w',encoding="utf8") as file_open:
        file_open.write(html_code)
        # Tách giá trị của mã nguồn cần tach
    soup = bs4.BeautifulSoup(html_code, 'html.parser')
    eles = soup.select('span')
            # Lấy giá trị vừa tách xong viết nó vào file mới
    with open(file='Checkex.txt', mode='w', encoding='utf8') as filename_check:
        for elem in eles:
            text = elem.get_text()
            filename_check.write(text + ' ')  
    filename_text = 'Checkex.txt'
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
    # print(text_btc)
    filename = 'PriceCoin.xlsx'
    # Tạo hàm Update giá trị trong Execl
    def Update_Excel(filename,paper_sheet,col_row,value) :
        workbook = openpyxl.load_workbook(filename=filename)
        sheet = workbook[paper_sheet]
        sheet[col_row].value = value
        workbook.close()
        workbook.save(filename=filename)
#Update Tên Trong File Execl
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='A1',value="Bitcoin")
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='A2',value="Houbi")
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='A3',value="Ape")
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='A4',value="Apt")
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='A5',value="Agix")   
#Update Giá Trị Coin Trong File Execl
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='B1',value=text_btc)
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='B2',value=text_hb)
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='B3',value=text_ape)
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='B4',value=text_apt)
        Update_Excel(filename=filename,paper_sheet='Sheet1',col_row='B5',value=text_agix)

