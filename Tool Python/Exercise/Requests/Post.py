# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')

# Sử dụng phương thức POST để gửi yêu cầu tới url https://httpbin.org/post bao gồm dữ liệu 'payload_post'. 
# Sau đó in ra Status Code và r_post.text.
url_post = "https://httpbin.org/post"
payload_post =  {"first name" : "Nick" ,"birtday" : "17-11-2004"}
r_post = requests.post(url=url_post, data=payload_post)
print("Status Code",r_post.status_code)
print(r_post.text)