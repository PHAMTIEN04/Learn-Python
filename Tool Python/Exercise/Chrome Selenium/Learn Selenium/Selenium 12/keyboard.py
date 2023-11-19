from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep


class KeyBoard:
    def __init__(self):
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.input1 = self.driver.find_element(By.XPATH,"//*[@id='name']")
        self.input2 = self.driver.find_element(By.XPATH,"//*[@id='email']")
        self.input1.send_keys("aaasadasdasda")
    def Ctrl_a(self):
        self.input1.send_keys(Keys.CONTROL,'a')
    def Ctrl_c(self):        
        self.input1.send_keys(Keys.CONTROL,'c')
    def Ctrl_v(self):
        self.input2.send_keys(Keys.CONTROL,'v')
    def close(self):
        sleep(100)
        self.driver.close()
        
k = KeyBoard()

k.Ctrl_a()
k.Ctrl_c()
k.Ctrl_v()
k.close()
        