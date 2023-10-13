# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Define the path to the Chrome WebDriver executable on your local system
path = r"D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

# Create a Service object, which specifies the path to the WebDriver executable
service = Service(executable_path=path)

# Create a Chrome driver instance and associate it with the Service
driver = Chrome(service=service)

# Navigate to a specific URL using the Chrome driver
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Print the title of the web page opened by the driver
print(driver.title)

# Print the current URL of the web page opened by the driver
print(driver.current_url)

# Print the page source code of the web page opened by the driver
print(driver.page_source)

# Pause the script for 100 seconds (useful for manual inspection or testing)
sleep(100)

# Close the Chrome driver, terminating the browser session
driver.close()
