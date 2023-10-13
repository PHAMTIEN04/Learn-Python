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
driver.get("https://money.rediff.com/gainers")

# Find an input element on the page using its XPath and print its text (which may be empty for an input element)
T_check = driver.find_element(By.XPATH, "//*[@id='srchword']")
print("Text: ", T_check.text)

# Find the same input element again and send the keys "deptrai" to it
T_check = driver.find_element(By.XPATH, "//*[@id='srchword']")
T_check.send_keys("deptrai")

# Retrieve the value attribute of the input element (which should be "deptrai" after sending keys)
print("Get attribute: ", T_check.get_attribute('value'))

# Pause the script for 10 seconds (useful for manual inspection or testing)
sleep(10)

# Close the Chrome driver, terminating the browser session
driver.close()
