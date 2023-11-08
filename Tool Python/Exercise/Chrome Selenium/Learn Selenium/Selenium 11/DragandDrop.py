# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for drag-and-drop functionality
class Drag_and_Drop:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

    def run(self):
        # Navigate to a website
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(10)

        # Find the source and target elements using XPath
        self.source = self.driver.find_element(By.XPATH, "//*[@id='draggable']")
        self.target = self.driver.find_element(By.XPATH, "//*[@id='droppable']")

        # Create an ActionChains object for performing the drag-and-drop action
        self.ac = ActionChains(driver=self.driver)

        # Perform the drag-and-drop action, moving the source element to the target element
        self.ac.drag_and_drop(source=self.source, target=self.target).perform()

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Drag_and_Drop class and run the script
d_d = Drag_and_Drop()
d_d.run()
