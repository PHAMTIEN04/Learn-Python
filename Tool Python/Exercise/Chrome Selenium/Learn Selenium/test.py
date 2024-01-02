from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = Chrome(service=service)


driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("zzz")
driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()
sleep(100)

driver.close()