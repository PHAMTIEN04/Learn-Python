from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from threading import Thread





url = str(input("Nhập Url: "))
class ViewX():

    def __init__(self):
        self.service = Service(executable_path="D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe")
        self.options = Options()
        # self.options.add_argument(f"--user-data-dir=D:/Learn Python/Tool Python/Project Buff View X/Run 11/Chrome data {i}")
        self.options.add_argument("--window-size=600,600")
        # self.options.add_argument('--blink-settings=imagesEnabled=false')
        self.options.add_argument("--incognito")
        self.options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
            )
        # self.options.add_argument("--headless")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = Chrome(service=self.service, options=self.options)

        self.driver.get(url)
        self.driver.implicitly_wait(30)
        # Login
        login = self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/span")
        login.click()
        # Account
        account = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input")
        account.send_keys("lvtuuyen2k@gmail.com")
        # Next
        self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div").click()
        # Password
        try:
            password = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password.send_keys("12312311Aa")
        
        # Next
            self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div").click()
        except:
            auth = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input")
            auth.send_keys("@TuUyen34255")
            self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span").click()
            password = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password.send_keys("12312311Aa")
        
        # Next
            self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div").click()
            
        self.num_check = ""
        while True:
            try:
                num_view = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[4]/div/div[1]/div/div[3]/span/div/span/span/span").text
                if self.num_check != num_view:
                    self.num_check = num_view
                    print("Views:", self.num_check)
                sleep(0.5)
            except:
                print("Error!!!")
                sleep(180)
            self.driver.refresh()
        # sleep(100)
        self.driver.close()

def viewx():
    view_x = ViewX()
# open_viewx()
if __name__ == "__main__":
    list_r = []
    size = 1
    for i in range(0,size):
        thread = Thread(target=viewx)
        list_r.append(thread)
    
    for th in list_r:
        th.start()
    
    for th in list_r:
        th.join()