from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import os
from pynput.keyboard import Key,Controller
import random
import pyautogui
import pygetwindow as gw

options = Options()
chrome_prefs = {
        "profile.default_content_setting_values": {"images": 1}
    }
    #1die
options.add_experimental_option("prefs", chrome_prefs)
options.add_argument(f"--user-data-dir=D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/Facebook Account/Account 2")
options.add_argument('--disable-notifications')
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/messages/t/100082676794528")

check = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/span[2]/div").click()


sleep(100)
driver.close()