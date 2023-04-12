# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')

# Sử dụng phương thức POST để tải lên các tệp tin 'Filecsv.csv'. 
# Yêu cầu được gửi đến url https://httpbin.org/post với cú pháp files. Sau đó in ra Status Code và r_file.text.
url_file = "https://httpbin.org/post" 
file = {
    'file1' : open('Filecsv.csv', 'rb'),
    'file2' : open('Filecsv.csv', 'rb'),
    'file3' : open('Filecsv.csv', 'rb')
    }
r_file = requests.post(url=url_file , files =file )
print(r_file.status_code)
print(r_file.text)