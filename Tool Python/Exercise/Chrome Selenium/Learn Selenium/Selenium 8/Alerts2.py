from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = Chrome(ChromeDriverManager().install())

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
sleep(5)
driver.get("https://mypage.rediff.com/")
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/form/table/tbody/tr[1]/td[3]/input").click()
checkalerts = driver.switch_to.alert
checkalerts.accept()
sleep(100)
driver.close()