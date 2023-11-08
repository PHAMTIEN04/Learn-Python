# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for mouse hovering functionality
class Mouse_Hover:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
    
    def run(self):
        # Navigate to a website
        self.driver.get("https://demo.automationtesting.in/Register.html")
        self.driver.implicitly_wait(10)

        # Find the elements for mouse hovering
        element1 = self.driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/a")
        element2 = self.driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
        element3 = self.driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a")

        # Create an ActionChains object for performing mouse hovering
        ac = ActionChains(driver=self.driver)
        ac.move_to_element(element1).move_to_element(element2).perform()

        # Click on the third element
        element3.click()

        # Check for the presence of an advertisement and close it if found
        try:
            qc = self.driver.find_element(By.XPATH, "//*[@id='dismiss-button']/div/span")
            print("Có Quảng Cáo (Advertisement is present)")
            qc.click()
            print("Đã Tắt Quảng Cáo (Advertisement has been closed)!!!")
        except:
            print("Không Có Quảng Cáo (No Advertisement)")

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Mouse_Hover class and run the script
m = Mouse_Hover()
m.run()
