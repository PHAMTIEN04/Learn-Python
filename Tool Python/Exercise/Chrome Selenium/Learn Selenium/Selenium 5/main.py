from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

path = r"D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

service = Service(executable_path=path)


driver = Chrome(service=service)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

select = driver.find_elements(By.CSS_SELECTOR, 'td')
cnt = 1
print(len(select))
for i in select:
    if i.text == "Stocks":
        
        break
    print(i.text,end=" ")
    cnt = cnt + 1
    if cnt == 6:
        print()
        cnt = 1
        




sleep(100)
driver.close()