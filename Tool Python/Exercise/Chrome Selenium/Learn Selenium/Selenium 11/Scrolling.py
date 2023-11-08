# Import necessary libraries and modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for scrolling functionality
class Scrolling:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()

    def run(self):
        # Navigate to a website
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.implicitly_wait(10)
        
        # Scroll to the bottom of the page using JavaScript
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        
        # Print the current vertical scroll position
        print(self.driver.execute_script("return window.pageYOffset;"))

        # Pause the script for 2 seconds
        sleep(2)

        # Scroll back to the top of the page using JavaScript
        self.driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
        
        # Print the current vertical scroll position (should be back to the top)
        print(self.driver.execute_script("return window.pageYOffset;"))

        # Pause the script for 100 seconds (you may want to use a more reasonable sleep time)
        sleep(100)

        # Close the web browser
        self.driver.close()

# Create an instance of the Scrolling class and run the script
scr = Scrolling()
scr.run()
