import bs4
import requests
import io
import re
import os
from time import sleep
from colorama import Fore, Style

os.chdir(r"C:\Learn Python\Tool Python\Project\Project UpdatePriceCoinTXT")
delay_time = 2

while True: #Vòng lặp vô hạn
    # Cho Try Except để check mã
    try:
        # Lấy mã nguồn
        url = 'https://coinmarketcap.com/'
        response = requests.get(url=url)
        html_code = response.text   
        filename = 'codetxt.html'
        # Cho mã nguồn vào file 
        with open(file=filename,mode='w',encoding="utf8") as file_open:
            file_open.write(html_code)
            # Tách giá trị của mã nguồn cần tacgs
        soup = bs4.BeautifulSoup(html_code, 'html.parser')
        eles = soup.select('span')
        # Lấy giá trị vừa tách xong viết nó vào file mới
        with open(file='Checktxt.txt', mode='w', encoding='utf8') as filename_check:
            for elem in eles:
                text = elem.get_text()
                filename_check.write(text + ' ')
                # Đọc giá tri của File 
        filename_text = 'Checktxt.txt'
        with open(file=filename_text, mode='r', encoding='utf8') as file_text:
            check_regex = file_text.read()
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
        # Làm đẹp
        text_all = "Bitcoin : " + text_btc +"\n" + "Houbi : " + text_hb + "\n" + "Ape : "+ text_ape + "\n" + "Apt : " + text_apt + "\n" + "Agix : " + text_agix
        # Tạo file mới để chứa các thông tin vừa Regex được
        filename_token = "Cointxt.txt"
        with open(file=filename_token,mode='w',encoding="utf8") as file_coin :
            file_coin.write(text_all)
            # Đọc File vừa regex được
        with open(file=filename_token, mode="r",encoding="utf8") as file_read_coin :
            read_coin = file_read_coin.read()
            print(Fore.GREEN, Style.BRIGHT) # cho màu và kiểu chữ
            print("Cập nhật thông tin Coin :\n")
            print(read_coin) # in ra giá trị của file đó
            sleep(delay_time) # Thời gian chờ
            print("\033[H\033[J") # clear screen
            # os.system('cls')
    except Exception as e:
        print(f"Lỗi: {e}")
        print("Đang chờ 5 giây để tiếp tục thực hiện...")
        sleep(5)

# Đoạn code này thực hiện việc lấy thông tin giá của một số loại tiền điện tử (Bitcoin, Huobi Token, ApeCoin, Aptos, SingularityNET) từ trang web CoinMarketCap.com và lưu vào file văn bản.

# Cụ thể, đoạn code thực hiện các công việc sau:

# Import các module cần thiết: bs4, requests, io, re, os, time, colorama
# Thiết lập thời gian chờ giữa các lần cập nhật giá của tiền điện tử bằng biến delay_time.
# Sử dụng vòng lặp vô hạn để liên tục cập nhật thông tin giá của các loại tiền điện tử.
# Gửi yêu cầu lấy mã HTML của trang CoinMarketCap.com bằng phương thức GET và lưu mã HTML vào biến html_code.
# Ghi mã HTML vào file code.html.
# Dùng BeautifulSoup để tìm các thẻ <span> trong mã HTML và lưu vào biến eles.
# Ghi nội dung của các thẻ <span> vào file văn bản Check.txt.
# Đọc nội dung của file Check.txt và lưu vào biến check_regex.
# Sử dụng regular expression để tìm thông tin giá của từng loại tiền điện tử từ biến check_regex.
# Ghi thông tin giá của các loại tiền điện tử vào file Coin.txt.
# Đọc nội dung của file Coin.txt và hiển thị thông tin giá các loại tiền điện tử lên màn hình.
# Xóa màn hình và tiếp tục vòng lặp để tiếp tục cập nhật thông tin giá của các loại tiền điện tử.
# Lưu ý rằng trong đoạn code này, các regular expression được sử dụng để tìm thông tin giá của các loại tiền điện tử là 
# cụ thể cho trang CoinMarketCap.com và có thể không áp dụng cho các trang web khác. Nếu muốn lấy thông tin giá từ các trang web khác, cần điều chỉnh lại các regular expression để phù hợp với định dạng của thông tin trên trang đó.