import requests

url = "https://httpbin.org/404"




try:
    r_err = requests.get(url=url,timeout=0.1)
    r_err.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error",e)
# Code này lấy một URL và sử dụng thư viện requests để thực hiện GET request tới đường dẫn đó (ở đây là "https://httpbin.org/404").
# Trong cổng try, nếu đoạn mã trong khối try (= requests.get() và raise_for_status()) gặp lỗi, nó sẽ quăng ra (throw) một RequestException.
# Ngoài ra, đã được sử dụng thêm time-out của 0.1 để giảm thiểu thời gian chờ đợi khi phản hồi từ máy chủ không có hoặc gặp sự cố trong việc phản hồi
# Vì vậy, trên cùng một dòng với except, e được gán cho các chi tiết liên quan đến lỗi và kèm theo thông điệp "Error" sau đó được in ra màn hình nếu xảy ra lỗi. 
# Nếu không có lỗi, thì bỏ qua except block.



