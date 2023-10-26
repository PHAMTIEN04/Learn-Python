# Import necessary libraries from Selenium and time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for managing notification popups
class Notification_Popup:
    def setup(self):
        # Create ChromeOptions to disable notifications
        self.ops = ChromeOptions()
        self.ops.add_argument("--disable-notifications")
        
        # Initialize the Chrome driver with the specified options
        self.driver = Chrome(executable_path=ChromeDriverManager().install(), options=self.ops)

    def N_P(self):
        # Open a website (https://whatmylocation.com/)
        self.driver.get("https://whatmylocation.com/")
        
        # Sleep for 100 seconds (simulate some action on the website)
        sleep(100)
        
        # Close the Chrome driver
        self.driver.close()

# Create an instance of the Notification_Popup class
n = Notification_Popup()

# Call the setup method to configure the Chrome driver
n.setup()

# Call the N_P method to open the website, perform actions, and close the driver
n.N_P()
