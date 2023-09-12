from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
import os
from multiprocessing import Pool


from time import sleep 

os.chdir(r"C:\Learn Python\Tool Python\Bài Tập\Chrome Selenium")



def t_driver(filePath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(
		"user-data-dir="+filePath)
    prefs = {
            "profile.managed_default_content_settings.images": 2
        }
    chrome_options.add_experimental_option("prefs", prefs)
    driver_path = "C:\Learn Python\Tool Python\Bài Tập\Chrome Selenium\chromedriver"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service,options=chrome_options)
    return driver

def rl_sub(filePath):
   
    js = "window.scrollBy(0,0.7*window.innerHeight)"
    driver = t_driver(filePath)
    driver.get("https://www.24h.com.vn/")
    while True:    
        driver.execute_script(js)
        sleep(2)

rl_sub('chrome')
# def poolprocess():
#     p = Pool(3)
#     kq = p.map_async(rl_sub,("https://www.24h.com.vn/","https://www.24h.com.vn/"))
    
#     print(kq.get())
#     p.close()
#     p.join()
    
# if __name__ == "__main__":
#     poolprocess()