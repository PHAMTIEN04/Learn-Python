# Importing necessary modules
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())

# Navigating to a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Adding a delay for demonstration purposes (100 seconds)
sleep(100)

# Closing the Chrome WebDriver
driver.close()
