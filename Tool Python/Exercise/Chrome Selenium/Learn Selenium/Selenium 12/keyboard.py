# Import necessary modules and classes from Selenium and other libraries
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# Define a class named KeyBoard to encapsulate the functionality
class KeyBoard:
    # Constructor method to initialize the WebDriver and open a webpage
    def __init__(self):
        # Initialize Chrome WebDriver using WebDriver Manager to automatically download the appropriate driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Set implicit wait to handle dynamic elements
        self.driver.implicitly_wait(10)
        
        # Open a test webpage for demonstration
        self.driver.get("https://testautomationpractice.blogspot.com/")
        
        # Locate input elements by XPath
        self.input1 = self.driver.find_element(By.XPATH, "//*[@id='name']")
        self.input2 = self.driver.find_element(By.XPATH, "//*[@id='email']")
        
        # Enter some text into the first input field
        self.input1.send_keys("aaasadasdasda")

    # Method to simulate pressing Ctrl+A (select all) on the first input field
    def Ctrl_a(self):
        self.input1.send_keys(Keys.CONTROL, 'a')

    # Method to simulate pressing Ctrl+C (copy) on the first input field
    def Ctrl_c(self):
        self.input1.send_keys(Keys.CONTROL, 'c')

    # Method to simulate pressing Ctrl+V (paste) on the second input field
    def Ctrl_v(self):
        self.input2.send_keys(Keys.CONTROL, 'v')

    # Method to close the browser after a delay for demonstration purposes
    def close(self):
        sleep(100)
        self.driver.close()

# Create an instance of the KeyBoard class
k = KeyBoard()

# Call the methods to perform keyboard actions
k.Ctrl_a()  # Select all text in the first input field
k.Ctrl_c()  # Copy the selected text
k.Ctrl_v()  # Paste the copied text into the second input field

# Close the browser window after a delay
k.close()
