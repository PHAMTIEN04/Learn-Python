# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from time import sleep

# Create a class named "HFrame"
class HFrame:
    # Initialize the WebDriver
    def setup(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = Chrome(ChromeDriverManager().install())

    # Function to check and interact with frames on a web page
    def checkframe(self):
        # Navigate to the test page
        self.driver.get("https://testautomationpractice.blogspot.com/")

        # Switch to a specific frame with ID "frame-one796456169"
        self.driver.switch_to.frame("frame-one796456169")

        # Find an element in the frame and enter text
        self.driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-0']").send_keys("Acccc")

        # Find a radio button in the frame using a Select dropdown
        dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-3']"))
        dropdown.select_by_value("Radio-2")

        # Uncomment the following line to switch back to the main page if multiple frames are involved
        # self.driver.switch_to.default_content()

        # Wait for 10 seconds
        sleep(10)

# Create an instance of the "HFrame" class
f = HFrame()

# Call the "setup" method to initialize the WebDriver
f.setup()

# Call the "checkframe" method to interact with frames on the web page
f.checkframe()
