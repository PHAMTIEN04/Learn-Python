# Importing necessary modules
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from time import sleep

# Path to the Chrome WebDriver executable
path = "D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

# Initializing the WebDriver service
service = Service(executable_path=path)

# Creating a Chrome WebDriver instance
driver = Chrome(service=service)

# Navigating to a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Adding a delay for demonstration purposes (100 seconds)
sleep(100)

# Closing the Chrome WebDriver
driver.close()
