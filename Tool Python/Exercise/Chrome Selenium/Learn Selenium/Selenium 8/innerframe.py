# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class named "Iframe"
class Iframe:
    # Initialize the WebDriver
    def setup(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = Chrome(ChromeDriverManager().install())

    # Function to check and interact with iframes on a web page
    def checkiframe(self):
        # Navigate to the test page containing iframes
        self.driver.get("https://demo.automationtesting.in/Frames.html")

        # Click on the link "Iframe with in an Iframe"
        self.driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

        # Switch to the outer iframe
        outframe = self.driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
        self.driver.switch_to.frame(outframe)

        # Switch to the inner iframe within the outer iframe
        inframe = self.driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
        self.driver.switch_to.frame(inframe)

        # Find an element in the inner iframe and enter text
        self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Iframe hihi")

        # Uncomment the following line to switch back to the parent frame
        # self.driver.switch_to.parent_frame()

        # Wait for 100 seconds
        sleep(100)

        # Close the browser
        self.driver.close()

# Create an instance of the "Iframe" class
i = Iframe()

# Call the "setup" method to initialize the WebDriver
i.setup()

# Call the "checkiframe" method to interact with iframes on the web page
i.checkiframe()
