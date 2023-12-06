# Import necessary modules and classes from Selenium and other libraries
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import getcwd

# Create a class for capturing screenshots using Selenium
class CaptureScreenShot:
    def __init__(self) -> None:
        # Initialize the Chrome web driver using the ChromeDriverManager to manage the driver version
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        
        # Set an implicit wait time of 10 seconds for the WebDriver
        self.driver.implicitly_wait(10)
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Navigate to a sample website (https://demo.nopcommerce.com/) for demonstration
        self.driver.get("https://demo.nopcommerce.com/")

    # Method to perform the screenshot capture and save it to a file
    def run(self):
        # Save a screenshot of the current browser window to the specified file path
        self.driver.save_screenshot(getcwd() + "\\Selenium 13\\image.png")
        
        # Additional methods for capturing screenshots with different formats (commented out for demonstration)
        # self.driver.get_screenshot_as_file()
        # self.driver.get_screenshot_as_base64()
        # self.driver.get_screenshot_as_png()
        
        # Pause the script for 100 seconds (for demonstration purposes, you may adjust this)
        sleep(100)
        
        # Close the browser window
        self.driver.close()

# Create an instance of the CaptureScreenShot class and execute the run method
c = CaptureScreenShot()
c.run()
