# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')


# Trong đoạn code trên:

# url_cookies là URL của trang web cần truy cập.
# Biến cookies là một từ điển chứa các cookie mà khách hàng muốn gửi cùng với yêu cầu HTTP.
# requests.get(url_cookies, cookies=cookies) thực hiện yêu cầu GET tới url chỉ định và gửi các cookies được chỉ định trong register Cookies của message header.
# r_cookies.text Trả về nội dung response khi yêu cầu được gửi đến.
# Về cơ bản, đoạn mã này giúp chèn hoặc bổ sung cookie vào tiêu đề yêu cầu HTTP.
url_cookies = "https://httpbin.org/cookies"

cookies = {"location" : "new york"}

r_cookies = requests.get(url_cookies, cookies=cookies)

print(r_cookies.text)


# Nó truy cập trang web Google và lấy ra giá trị của một cookie được đặt tên là 1P_JAR từ phiên làm việc của trang web đó. 
# Ở đây r_jar.cookies["1P_JAR"] truy cập một dictionary để xác định giá trị của cookie đó bằng cách sử dụng ID 1P_JAR.
r_jar = requests.get("https://www.google.com")
print(r_jar.status_code)
print(r_jar.cookies["1P_JAR"])





# Trong đoạn code này, chúng ta sử dụng thư viện requests để tạo và gửi yêu cầu GET HTTP tới url "https://httpbin.org/cookies". 
# Chúng ta đã tạo một biến requestsJar của loại RequestsCookieJar trong thư viện cookies requests được sử dụng để lưu các cookie 
# mà chúng ta muốn đính kèm vào yêu cầu từ phía client.

# Sau đó, chúng ta đã sử dụng phương thức 'set()' để thiết lập cookie userid=join với domain là httpbin.org và path là /cookies. 
# Điều này có nghĩa là khi server nhận được yêu cầu từ phía client, cookie sẽ được thêm vào trong header của yêu cầu và được gửi về với các giá trị đi kèm.

# Cuối cùng, chúng ta gửi yêu cầu GET HTTP với thông số cookies được đặt và lưu trữ trong requestsJar. 
# Sau đó, nội dung của phản hồi từ máy chủ được in ra bằng phương thức 'text()'.

# Kết quả trả về sẽ hiển thị tất cả các cookie được gửi đến và nhận từ server.
url = "https://httpbin.org/cookies"
requestsJar = requests.cookies.RequestsCookieJar()
requestsJar.set("userid","join", domain = "httpbin.org", path = "/cookies")

r_ck = requests.get(url,cookies=requestsJar)
print(r_ck.text)