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

# Navigate to the first URL using the Chrome driver
driver.get("https://www.orangehrm.com/")

# Navigate to a second URL using the same Chrome driver
driver.get("https://money.rediff.com/index.html")

# Go back to the previous page (in this case, "https://www.orangehrm.com/")
driver.back()

# Go forward to the next page (in this case, "https://money.rediff.com/index.html")
driver.forward()

# Refresh the current page
driver.refresh()

# Pause the script for 10 seconds (useful for manual inspection or testing)
sleep(10)

# Close the Chrome driver, terminating the browser session
driver.close()
