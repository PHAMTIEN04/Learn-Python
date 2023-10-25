# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class named "Alerts2"
class Alerts2:
    # Initialize the WebDriver
    def setup(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = Chrome(ChromeDriverManager().install())
    
    # Function to check and handle a basic authentication alert
    def checkalerts(self):
        # Navigate to a page with basic authentication using the URL format: http://username:password@website.com
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
        
        # Wait for 5 seconds to allow the basic authentication to complete
        sleep(5)

        # Navigate to another page (in this case, "https://mypage.rediff.com/")
        self.driver.get("https://mypage.rediff.com/")

        # Find an element on the page and click it (this action triggers an alert)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/table/tbody/tr[1]/td[3]/input").click()

        # Switch to the alert dialog
        checkalerts = self.driver.switch_to.alert

        # Accept the alert (click OK)
        checkalerts.accept()

        # Wait for 100 seconds before closing the browser
        sleep(100)
        self.driver.close()

# Create an instance of the "Alerts2" class
check = Alerts2()

# Call the "setup" method to initialize the WebDriver
check.setup()

# Call the "checkalerts" method to test and handle a basic authentication alert
check.checkalerts()
