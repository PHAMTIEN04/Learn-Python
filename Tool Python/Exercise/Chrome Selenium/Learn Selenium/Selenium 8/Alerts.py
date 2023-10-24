from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
try:
    checkalerts = driver.switch_to.alert
    print(checkalerts.text)
    sleep(3)
    checkalerts.accept()
    driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button").click()
    print(checkalerts.text)
    sleep(3)
    checkalerts.dismiss()
    driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
    checkalerts.send_keys("Hihi")
    sleep(3)
    checkalerts.accept()
except:
    print("No Such Alerts!!!")
sleep(100)
driver.close()