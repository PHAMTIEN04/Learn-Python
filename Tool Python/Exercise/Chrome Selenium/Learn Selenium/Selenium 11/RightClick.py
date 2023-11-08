# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for right-click functionality
class Right_Click:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
    
    def run(self):
        # Navigate to a website
        self.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        self.driver.implicitly_wait(10)

        # Create an ActionChains object for performing a right-click action
        ac = ActionChains(driver=self.driver)

        # Find the element to right-click using XPath
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/p/span")

        # Perform the right-click action on the element
        ac.context_click(element).perform()

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Right_Click class and run the script
r = Right_Click()
r.run()
