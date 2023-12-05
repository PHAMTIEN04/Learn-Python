from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep  

# Khởi tạo trình duyệt và mở trang web

service = Service(executable_path='D:/Learn Python/Tool Python/Project AutoTyping/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://www.nettruyenus.com/truyen-tranh/hoc-gia-kiem-si/chap-85/1057964")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'id')))

get_id = driver.find_element(By.CSS_SELECTOR,"id")

for i in range(len(get_id)):
    print(get_id[i])


sleep(100)

# Đóng trình duyệt khi bạn đã hoàn thành
driver.quit()
