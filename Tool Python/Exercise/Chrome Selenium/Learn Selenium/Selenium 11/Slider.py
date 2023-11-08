# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for slider interaction
class Slider:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

    def run(self):
        # Navigate to a website
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(10)

        # Find the slider element using XPath
        self.slide = self.driver.find_element(By.XPATH, "//*[@id='slider']/span")

        # Print the initial location of the slider
        print(self.slide.location)

        # Create an ActionChains object for dragging the slider by a specified offset
        ac = ActionChains(driver=self.driver)
        ac.drag_and_drop_by_offset(self.slide, 100, 0).perform()

        # Print the updated location of the slider after dragging it
        print(self.slide.location)

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Slider class and run the script
s = Slider()
s.run()
