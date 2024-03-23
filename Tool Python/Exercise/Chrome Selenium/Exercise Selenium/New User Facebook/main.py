from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import os
from pynput.keyboard import Key,Controller
# D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account 0
import pyautogui
import pygetwindow as gw
options = Options()
chrome_prefs = {
    "profile.default_content_setting_values": {"images": 1}
}
options.add_experimental_option("prefs", chrome_prefs)
options.add_argument(f"--user-data-dir=D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/Facebook account/Account 0")
options.add_argument('--disable-notifications')
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div /div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[2]/ div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
driver = Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://www.facebook.com/")
# sleep(100)
driver.get("https://www.facebook.com/messages/t/100064994050342")

# f = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div[2]/span/span")
# f.click()
f1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/p")
f1.send_keys("aaaa",Keys.ENTER)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/div").click()
sleep(3)


# Find the window with the title "Open"
open_windows = gw.getWindowsWithTitle("Open")

# Check if any windows are found
if open_windows:
    # If windows are found, activate the first one
    open_window = open_windows[0]
    
    # Activate the window
    open_window.activate()

    # Wait briefly for the window to become active
    sleep(0.5)

    # Type the file path
    file_path = os.getcwd() + "\\1.png"
    pyautogui.write(file_path)
    sleep(0.5)
    # Press Enter
    pyautogui.press("tab")
    pyautogui.press("enter")
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div").click()
else:
    print("Window with the title 'Open' not found.")
# f2.send_keys("D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/New User Facebook/1.png",Keys.ENTER)

# for i in range(10):
#     f = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[{i+1}]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a")
#     print(f.get_attribute('href'))
# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
sleep(1000)
driver.close()
