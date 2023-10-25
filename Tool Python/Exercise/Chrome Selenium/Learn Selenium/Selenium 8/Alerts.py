# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class named "Alerts"
class Alerts:
    # Initialize the WebDriver
    def setup(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = Chrome(ChromeDriverManager().install())

    # Function to check and handle JavaScript alerts
    def checkalerts(self):
        # Navigate to the test page with JavaScript alerts
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Click the first button to trigger an alert
        self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()

        try:
            # Switch to the alert dialog
            checkalerts = self.driver.switch_to.alert

            # Print the text from the alert
            print(checkalerts.text)

            # Wait for 3 seconds
            sleep(3)

            # Accept the alert (click OK)
            checkalerts.accept()

            # Click the second button to trigger a confirmation alert
            self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()

            # Attempt to print the text from the confirmation alert (this will fail)
            print(checkalerts.text)

            # Wait for 3 seconds
            sleep(3)

            # Dismiss the confirmation alert (click Cancel)
            checkalerts.dismiss()

            # Click the third button to trigger a prompt alert
            self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()

            # Send the text "Hihi" to the prompt alert
            checkalerts.send_keys("Hihi")

            # Wait for 3 seconds
            sleep(3)

            # Accept the prompt alert (click OK)
            checkalerts.accept()

        except:
            # Handle the case where there are no such alerts
            print("No Such Alerts!!!")

        # Wait for 100 seconds before closing the browser
        sleep(100)
        self.driver.close()

# Create an instance of the "Alerts" class
check = Alerts()

# Call the "setup" method to initialize the WebDriver
check.setup()

# Call the "checkalerts" method to test and handle JavaScript alerts
check.checkalerts()
