from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re

# Set up Selenium driver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    prefs = {
        "profile.managed_default_content_settings.images": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver_path = "C:\Learn Python\Tool Python\Project Chromeselenium\chromedriver"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

# Load account credentials from file
def load_accounts(filename):
    lines = []
    with open(file=filename, mode="r", encoding="utf8") as file_account_fb:
        for line in file_account_fb:
            lines.append(line.strip())
    return lines

# Login to Facebook using given credentials
def login_to_facebook(driver, email, password):
    driver.get("https://mbasic.facebook.com/")
    acccount = driver.find_element(By.NAME, 'email')
    password_elem = driver.find_element(By.NAME, 'pass')
    acccount.send_keys(email)
    sleep(2)
    password_elem.send_keys(password, Keys.ENTER)
    sleep(2)

# Like a Facebook post
def like_facebook_post(driver, post_url):
    js_scroll_to_post = "document.querySelector('.bo.bp.bq.br.bs').click()"
    js_like_post = "document.querySelector('.cq').click()"
    
    driver.execute_script(js_scroll_to_post)
    driver.get(post_url)
    driver.execute_script(js_like_post)
    sleep(5)

# Main function to run the program
def main():
    os.chdir(r"C:\Learn Python\Tool Python\Project Chromeselenium")
    driver = setup_driver()
    accounts = load_accounts('account.txt')
    
    for account in accounts:
        regex_acc = re.compile(r"tk (.*?) :")
        kq_acc = regex_acc.search(account)
        email = kq_acc.group(1)
        regex_pass = re.compile(r"mk (.*)")
        kq_pass = regex_pass.search(account)
        password = kq_pass.group(1)
        
        login_to_facebook(driver, email, password)
        like_facebook_post(driver, "https://mbasic.facebook.com/permalink.php?story_fbid=pfbid0a1UHXgxk7XbHuW4eLVJfZ5JPBsfXDwpjsJeuwW2GbSpDWzX68FHbLwCFeXFrenG1l&id=100078977383223")
    
    driver.quit()

if __name__ == '__main__':
    main()

# Đây là một chương trình sử dụng Selenium để tự động thích một bài đăng trên Facebook bằng nhiều tài khoản Facebook khác nhau được lưu trong file "account.txt".

# Đầu tiên, chương trình khởi tạo một số tùy chọn cho trình duyệt Chrome để sử dụng ở chế độ ẩn danh và tắt hình ảnh.
# Sau đó, chương trình đọc từng tài khoản Facebook từ file "account.txt", đăng nhập vào Facebook bằng từng tài khoản này, tìm bài đăng đã được chỉ định bằng link 
# "link_post", và thích bài đăng này bằng cách thực thi JavaScript bằng "js_like".
# Chương trình sẽ chờ 5 giây sau khi đã thích bài đăng, trước khi đăng xuất khỏi tài khoản Facebook hiện tại và tiếp tục thực hiện với tài khoản Facebook tiếp theo 
# trong file "account.txt".



