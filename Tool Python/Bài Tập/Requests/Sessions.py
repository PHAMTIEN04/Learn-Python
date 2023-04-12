import requests

s = requests.Session()

username = {"Username" : "NICK"}
location = {"Location" : "USA"}
url_set_cookies = 'https://httpbin.org/cookies/set'
url_cookies = 'https://httpbin.org/cookies'

s.get(url_set_cookies,data=username)
s.get(url_set_cookies,data=location)

r = s.get(url_cookies)
print(r.text)
# Đoạn mã này tạo một requests.Session object và sử dụng đối tượng này để giữ các cookie giữa các request khác nhau. 
# Sau đó, một số cookies được set thông qua URL 'https://httpbin.org/cookies/set'. Tiếp theo là một GET request đến URL
# 'https://httpbin.org/cookies', in nội dung của response ra màn hình bao gồm cả cookie đã được lưu trữ từ 2 GET requests trước đó.
