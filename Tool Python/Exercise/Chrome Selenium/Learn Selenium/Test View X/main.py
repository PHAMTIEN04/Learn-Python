from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from multiprocessing import Process


class ViewX():
    num_check = ""

    def __init__(self):
        self.service = Service(executable_path="D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe")
        self.options = Options()
        self.options.add_argument("--user-data-dir=D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Learn Selenium/chrome data")
        self.options.add_argument("--window-size=600,600")
        self.driver = Chrome(service=self.service, options=self.options)
        self.driver.get("https://twitter.com/PhmTin09984454/status/1718828946635252075")
        self.driver.implicitly_wait(10)

    def run(self):
        while True:
            try:
                num_view = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[4]/div/div[1]/div/div[3]/span/div/span/span/span").text
                if ViewX.num_check != num_view:
                    ViewX.num_check = num_view
                    print("Views:", ViewX.num_check)
                sleep(2)
            except:
                sleep(180)
            self.driver.refresh()

        self.driver.close()

def open_viewx():
    view_x = ViewX()
    view_x.run()

if __name__ == "__main__":
    open_viewx()