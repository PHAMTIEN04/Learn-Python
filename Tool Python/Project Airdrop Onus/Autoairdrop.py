from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent

from time import sleep
import os


os.chdir(r"D:/Learn Python/Tool Python/Project Airdrop Onus")
# proxy_address = "34.238.235.194	"
# proxy_port = "80"

# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = f"{proxy_address}:{proxy_port}"
# proxy.ssl_proxy = f"{proxy_address}:{proxy_port}"

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
prefs = {
        "profile.managed_default_content_settings.images": 2
}
options.add_experimental_option('prefs',prefs)
driver_path = "D:/Learn Python/Tool Python/Project Airdrop Onus/chromedriver"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service,options=options)


user_agent = UserAgent()
random_user_agent = user_agent.random
options1 = webdriver.ChromeOptions()
options1.add_argument('--incognito')
prefs1 = {
        "profile.managed_default_content_settings.images": 2
}
options1.add_experimental_option('prefs',prefs1)
options1.add_argument('--proxy-server=http://162.223.94.164:80')

# options1.add_argument('--proxy-server=http://{}:{}'.format(proxy_address, proxy_port))

driver_path1 = "D:/Learn Python/Tool Python/Project Airdrop Onus/chromedriver"
service1 = Service(executable_path=driver_path1)
driver1 = webdriver.Chrome(service=service1,options=options1)


options2 = webdriver.ChromeOptions()
options2.add_argument('--incognito')
prefs2 = {
        "profile.managed_default_content_settings.images": 2
}
options2.add_experimental_option('prefs',prefs2)
driver_path2 = "D:/Learn Python/Tool Python/Project Airdrop Onus/chromedriver"
service2 = Service(executable_path=driver_path2)
driver2 = webdriver.Chrome(service=service2,options=options2)
driver2.get("https://10minutemail.net/")
i_element = driver2.find_element(By.ID,("fe_text"))

get_value_mail = i_element.get_attribute("value")
print(get_value_mail)


driver1.get("https://signup.goonus.io/")



account_reg = driver1.find_element(By.NAME,'account_reg')
account_reg.send_keys(get_value_mail)
password_reg = driver1.find_element(By.NAME,'password_reg')
fullname_reg = driver1.find_element(By.NAME,'fullname_reg')
import random 
text = ["A", "B", "C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K"
        ,"L" ,"M", "N", "O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z",
        "a", "b", "c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k"
        ,"l" ,"m", "n", "o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z",
        "1","2","3","4","5","6","7","8","9","0"

]
l = [9,10,11,12,13,14,15,16]
l_r = random.choice(l)
r_pass = random.choices(text,k=l_r )
print(r_pass)
password_reg.send_keys(r_pass)

list_fullname = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Quách", "Trương", "Võ", "Đinh", "Lương", "Lỗ", "Chử", "Mai", "Thái", "Tô", "Đoàn", "Hứa", "Thanh", "Đào", "Đỗ", "Thủy", "Lưu", "Tiền", "Kiều", "Trịnh", "Chu", "Lữ", "Khương", "Tăng", "Khoa", "Tiêu", "Ninh", "Phí", "Uông", "Châu", "Khâu", "Vi", "Lã", "Giang", "Tôn", "Kỷ", "Tăng", "Viên", "Khâu", "Viên", "Tiếp", "Sơn", "Dục", "Tôn", "Đoàn", "Tề", "Tử", "Vương", "Thường", "Phong", "Thiên", "Hoài", "Tiến", "Hiếu", "Mạnh", "Ngọc", "Huy", "Hiệp", "Tùng", "Hùng", "Bảo", "An", "Quân", "Bình", "Hải", "Xuân", "Minh", "Dũng", "Tân", "Phúc", "Quang", "Trung", "Hải", "Hà", "Việt", "Công", "Quốc", "Thắng", "Thành", "Lực", "Quyết", "Thịnh", "Vân", "Hào", "Anh"]
name_r = random.choices(list_fullname,k = 2)
print(name_r)
name1 = name_r[0]
name2 = name_r[1]
name = name1 + " " + name2
fullname_reg.send_keys(name)

checkbox_element = driver1.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox_element.click()
checkbox_element.send_keys(Keys.ENTER)

reg = "document.querySelector('.text').click()"
driver1.execute_script(reg)

sleep(120)
reset_mail = "document.querySelector('.fa.fa-refresh.fa-fw.fa-lg ').click()"
driver2.execute_script(reset_mail)

driver2.refresh()

click_mail = "document.querySelector('.row-link').click()"
driver2.execute_script(click_mail)

span_element = driver2.find_element(By.XPATH,"//span[text()='Activate now']")
span_element.click()


driver.get("https://earn.goonus.io/projects/ONUS-Airdrop-USDT?eid=sHQvR-ftZqUal5-I")

element = driver.find_element(By.XPATH,"//button[contains(text(), 'Tham gia Airdrop')]")
element.click()


sleep(1000)
driver.quit()
