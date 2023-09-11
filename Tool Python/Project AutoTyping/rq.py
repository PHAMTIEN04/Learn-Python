from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  

# Khởi tạo trình duyệt và mở trang web
driver = webdriver.Chrome(executable_path='D:/Learn Python/Tool Python/Bài Tập/Chrome Selenium/chromedriver')
driver.get("https://10fastfingers.com/competition/64fe1ddddd351")
sleep(5)
js_click = "document.querySelectorAll('.CybotCookiebotDialogBodyButton')[1].click()"
driver.execute_script(js_click)
# Chờ cho trang web được tải hoàn toàn
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'row1')))

# Sử dụng Selenium để lấy danh sách các phần tử span trong thẻ div
div_element = driver.find_element(By.ID, 'row1')
span_elements = div_element.find_elements(By.CSS_SELECTOR, 'span')  # Sử dụng find_elements thay vì find_element

# Lặp qua danh sách các phần tử span và lấy nội dung của từng phần tử
text_data = ""
for span_element in range(len(span_elements)):
    # span_text = span_elements[span_element].text
    print("Content of a span element:", span_elements[span_element].text)
    with open("data.txt","w") as file:
        text_data = text_data + span_elements[span_element].text + "\n"
        file.write(text_data)
    if span_elements[span_element+1].text == "" :
        break
    

sleep(100)

# Đóng trình duyệt khi bạn đã hoàn thành
driver.quit()
