from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# class Tab_and_Windows:
#     def __init__(self):
#         self.driver = Chrome(executable_path=ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.driver.get("https://text-compare.com/")
#         self.driver.switch_to.new_window("tab")
#         self.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    
#     def tab(self):
#         pass
    
#     def close(self):
        
#         sleep(100)
#         self.driver.close()
        
        
# taw = Tab_and_Windows()
# taw.close()
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="D:\Learn Python\Tool Python\Exercise\Chrome Selenium\chromedriver.exe")
driver = Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

sleep(100)
driver.close()