# Tải module webdriver từ package selenium.
from selenium import webdriver 

# Tải module By từ package selenium.webdriver.common.by. Nó giúp chọn phương thức tìm kiếm phù hợp trong việc tìm element.
from selenium.webdriver.common.by import By

# Tải module WebDriverWait từ package selenium.webdriver.support.ui. Nó cung cấp các hàm để đợi cho đến khi một điều kiện nhất định được thỏa mãn trước khi tiếp tục thực hiện các lệnh khác.
from selenium.webdriver.support.ui import WebDriverWait

# Chức năng khởi động và quản lý quá trình ChromeDriver từ xa.
from selenium.webdriver.chrome.service import Service

# Tải module expected_conditions và đặt tên tắt là ec. Module này chứa các hàm kiểm tra các điều kiện dành cho WebDriverWait.
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.keys import Keys

from time import sleep  

def click_js(js):
    js_reg = js
    driver.execute_script(js_reg)
    

while True :
    
# Khởi tạo options 
    options = webdriver.ChromeOptions()

    prefs = {
        "profile.managed_default_content_settings.images": 2
    }
    options.add_experimental_option("prefs", prefs)

# Tạo đường dẫn tới chromedriver, dựa trên nơi lưu trữ của bạn
    driver_path = "C:\Learn Python\Tool Python\Bài Tập\Chrome Selenium\chromedriver"

# Tạo một đối tượng Service
    service = Service(executable_path=driver_path)
# Khởi tạo driver
    driver = webdriver.Chrome(service=service, options=options)

# Khởi tạo WebDriver
    driver.get("https://muasubre.vn/")
# Thực thi click bằng js
    click_js("document.querySelectorAll('.nav-link')[1].click()")

    fullname = str(input("Nhập Full Name :"))
    mail = str(input("Nhập Mail :"))
    account =str(input("Nhập account :"))
    password = str(input("Nhập password :"))

# Điền vào input bằng driver
    reg_fullname = driver.find_element(By.NAME,"fullname")
    reg_mail = driver.find_element(By.NAME, "email")
    reg_account = driver.find_element(By.NAME, "username")
    reg_password = driver.find_element(By.NAME, "password")

    reg_fullname.send_keys(fullname)
    sleep(1)
    reg_mail.send_keys(mail)
    sleep(1)
    reg_account.send_keys(account)
    sleep(1)
    reg_password.send_keys(password,Keys.ENTER)
    
# Thực thi click bằng js
    click_js("document.querySelector('.swal2-confirm.swal2-styled.swal2-default-outline').click()")

    login_account = driver.find_element(By.NAME, "username")
    login_password = driver.find_element(By.NAME, "password")
    login_account.send_keys(account)
    sleep(1)
    login_password.send_keys(password,Keys.ENTER)
    sleep(2)

    driver.quit()