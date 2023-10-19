# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())
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
