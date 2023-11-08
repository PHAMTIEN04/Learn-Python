# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for double-click functionality
class Double_Click:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

    def run(self):
        # Navigate to a website
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(10)

        # Find the button element using XPath
        element = self.driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

        # Clear and input text into a field
        self.driver.find_element(By.XPATH, "//*[@id='field1']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='field1']").send_keys("Tien DepTrai")

        # Create an ActionChains object for performing double-click action
        ac = ActionChains(driver=self.driver)

        # Perform a double-click action on the button element
        ac.double_click(element).perform()

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Double_Click class and run the script
d = Double_Click()
d.run()
