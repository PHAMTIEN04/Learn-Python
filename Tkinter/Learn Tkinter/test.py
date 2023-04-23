import requests 
import re
import bs4


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
kq_btc = regex_btc.search(check_regex)
text_btc = kq_btc.group(1)
print(text_btc)