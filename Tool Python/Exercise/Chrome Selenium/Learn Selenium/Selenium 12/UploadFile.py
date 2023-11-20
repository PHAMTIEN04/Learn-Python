# Import necessary modules and classes from Selenium and other libraries
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Define a class named UploadFile to encapsulate the functionality
class UploadFile:
    # Constructor method to initialize the WebDriver and open a webpage
    def __init__(self):
        # Initialize Chrome WebDriver using WebDriver Manager to automatically download the appropriate driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Set implicit wait to handle dynamic elements
        self.driver.implicitly_wait(10)
        
        # Open a webpage with a file upload button for demonstration
        self.driver.get("https://www.file.io/")

    # Method to simulate uploading a file using a file input element
    def upload(self):
        # Find the file input element by XPath and provide the file path for upload
        file_input = self.driver.find_element(By.XPATH, "//*[@id='upload-button']")
        file_input.send_keys("D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Learn Selenium/Selenium 12/File Test/file-sample_100kB.doc")
        # Note: In a real scenario, you would use the actual path of the file you want to upload

    # Method to close the browser after a delay for demonstration purposes
    def close(self):
        sleep(100)
        self.driver.close()

# Create an instance of the UploadFile class
u = UploadFile()

# Call the upload method to simulate uploading a file
u.upload()

# Close the browser window after a delay
u.close()


#EX Elements to Upload: <input type="file" class="...">