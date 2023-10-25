# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class named "BrowserWindow"
class BrowserWindow:
    # Initialize the WebDriver
    def setup(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = Chrome(ChromeDriverManager().install())

    # Function to check and manage browser windows
    def checkbw(self):
        # Set an implicit wait time for the WebDriver to wait for elements to load
        self.driver.implicitly_wait(30)

        # Navigate to the OrangeHRM login page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Click the link with the text "OrangeHRM, Inc"
        self.driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

        # Get the ID of the current window (single ID browser window)
        windowID = self.driver.current_window_handle
        print("ID:", windowID)

        # Get the IDs of all open browser windows (multiple ID browser windows)
        windowIDs = self.driver.window_handles
        print("ID's:", windowIDs)

        # Switch back to the first browser window
        self.driver.switch_to.window(windowIDs[0])

        # Loop through each window and print the title of each browser
        for id in windowIDs:
            self.driver.switch_to.window(id)
            print("Title Browser: ", self.driver.title)

        # Wait for 100 seconds before closing the browser
        sleep(100)
        self.driver.close()

# Create an instance of the "BrowserWindow" class
bw = BrowserWindow()

# Call the "setup" method to initialize the WebDriver
bw.setup()

# Call the "checkbw" method to manage browser windows
bw.checkbw()
