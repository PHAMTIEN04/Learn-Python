# Import necessary modules and classes from Selenium and other libraries
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import os
from time import sleep

# Define a class named FileDownload to encapsulate the functionality
class FileDownload:
    # Constructor method to initialize the WebDriver and open a webpage
    def __init__(self):
        # Get the current working directory
        location = os.getcwd()
        
        # Configure Chrome options for file download
        ops = ChromeOptions()
        
        # Set the default download directory path
        pre = {"download.default_directory": "D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Learn Selenium\Selenium 12\File Test"}
        ops.add_experimental_option("prefs", pre)
        
        # Initialize Chrome WebDriver using WebDriver Manager to automatically download the appropriate driver
        self.driver = Chrome(executable_path=ChromeDriverManager().install(), options=ops)
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Set implicit wait to handle dynamic elements
        self.driver.implicitly_wait(10)
        
        # Open a webpage with a file download link for demonstration
        self.driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

    # Method to simulate clicking a download link and initiating file download
    def download(self):
        # Find the download link element and retrieve its href attribute (URL)
        download_link = self.driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a")
        download_url = download_link.get_attribute('href')
        print(download_url)
        
        # Open the download URL to initiate the file download
        self.driver.get(download_url)

    # Method to close the browser after a delay for demonstration purposes
    def close(self):
        sleep(100)
        self.driver.close()

# Create an instance of the FileDownload class
f = FileDownload()

# Call the download method to initiate file download
f.download()

# Close the browser window after a delay
f.close()
