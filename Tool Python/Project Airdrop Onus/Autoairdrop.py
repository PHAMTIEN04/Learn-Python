from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent
import string
import random
from time import sleep
import os
import cv2
import pytesseract
from PIL import Image

# Set the project directory
project_directory = os.path.abspath("D:/Learn Python/Tool Python/Project Airdrop Onus")
os.chdir(project_directory)

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
prefs = {
    "profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument(f'user-agent={UserAgent().random}')

# Set the driver path
driver_path = os.path.join(project_directory, "chromedriver")
service = Service(executable_path=driver_path)

# Create driver instances
driver = webdriver.Chrome(service=service, options=chrome_options)
driver1 = webdriver.Chrome(service=service, options=chrome_options)
driver2 = webdriver.Chrome(service=service, options=chrome_options)

# Get the email address from 10minutemail.net
driver2.get("https://10minutemail.net/")
email_element = driver2.find_element(By.ID, "fe_text")
email_address = email_element.get_attribute("value")
print(email_address)

# Register on signup.goonus.io
driver1.get("https://signup.goonus.io/6277729712534476702")
account_reg = driver1.find_element(By.NAME, 'account_reg')

# Generate a random password
password_reg = driver1.find_element(By.NAME, 'password_reg')
password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.choice([9, 10, 11, 12, 13, 14, 15, 16])))
print(password)

# Generate a random full name
list_fullname = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Quách", "Trương", "Võ", "Đinh", "Lương", "Lỗ", "Chử", "Mai", "Thái", "Tô", "Đoàn", "Hứa", "Thanh", "Đào", "Đỗ", "Thủy", "Lưu", "Tiền", "Kiều", "Trịnh", "Chu", "Lữ", "Khương", "Tăng", "Khoa", "Tiêu", "Ninh", "Phí", "Uông", "Châu", "Khâu", "Vi", "Lã", "Giang", "Tôn", "Kỷ", "Tăng", "Viên", "Khâu", "Viên", "Tiếp", "Sơn", "Dục", "Tôn", "Đoàn", "Tề", "Tử", "Vương", "Thường", "Phong", "Thiên", "Hoài", "Tiến", "Hiếu", "Mạnh", "Ngọc", "Huy", "Hiệp", "Tùng", "Hùng", "Bảo", "An", "Quân", "Bình", "Hải", "Xuân", "Minh", "Dũng", "Tân", "Phúc", "Quang", "Trung", "Hải", "Hà", "Việt", "Công", "Quốc", "Thắng", "Thành", "Lực", "Quyết", "Thịnh", "Vân", "Hào", "Anh"]
name = ' '.join(random.choices(list_fullname, k=2))
print(name)
fullname_reg = driver1.find_element(By.NAME, 'fullname_reg')

# Checkbox handling options
checkbox_element = driver1.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox_options = [
    (account_reg, password_reg, fullname_reg),
    (account_reg, fullname_reg, password_reg),
    (password_reg, account_reg, fullname_reg),
    (fullname_reg, account_reg, password_reg)
]
random.shuffle(checkbox_options)

for account_element, password_element, fullname_element in checkbox_options:
    checkbox_element.click()
    account_element.send_keys(email_address)
    password_element.send_keys(password)
    fullname_element.send_keys(name)

    # Check if CAPTCHA is present
# Check if CAPTCHA is present
captcha_element = driver1.find_element(By.CSS_SELECTOR, "img.captcha")
if captcha_element:
    # Process the CAPTCHA image
    captcha_image_url = captcha_element.get_attribute("src")
    driver1.save_screenshot("screenshot.png")
    location = captcha_element.location
    size = captcha_element.size
    left = int(location['x'])
    top = int(location['y'])
    right = int(location['x'] + size['width'])
    bottom = int(location['y'] + size['height'])
    image = cv2.imread("screenshot.png")
    captcha_image = image[top:bottom, left:right]
    captcha_image_path = os.path.join(project_directory, "captcha_image.png")
    cv2.imwrite(captcha_image_path, captcha_image)

    # Process the CAPTCHA image using OCR
    captcha_text = pytesseract.image_to_string(Image.open(captcha_image_path))

    if captcha_text:
        captcha_input = driver1.find_element(By.NAME, 'captcha')
        captcha_input.send_keys(captcha_text)
        

        
    checkbox_element.click()
    account_element.clear()
    password_element.clear()
    fullname_element.clear()

# Submit the form
reg = "document.querySelector('.text').click()"
driver1.execute_script(reg)

# Wait for email activation and activate the account
sleep(120)
reset_mail = "document.querySelector('.fa.fa-refresh.fa-fw.fa-lg ').click()"
driver2.execute_script(reset_mail)
driver2.refresh()

click_mail = "document.querySelector('.row-link').click()"
driver2.execute_script(click_mail)

span_element = driver2.find_element(By.XPATH, "//span[text()='Activate now']")
span_element.click()

# Access the ONUS Airdrop project
driver.get("https://earn.goonus.io/projects/ONUS-Airdrop-USDT?eid=sHQvR-ftZqUal5-I")

element = driver.find_element(By.XPATH, "//button[contains(text(), 'Tham gia Airdrop')]")
element.click()

# Quit the drivers
driver.quit()
driver1.quit()
driver2.quit()
