# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Navigate to the "https://testautomationpractice.blogspot.com/" website
driver.get("https://testautomationpractice.blogspot.com/")

## 1) Select a specific checkbox
# Approach 1: Select a checkbox by its ID
# driver.find_element(By.ID, "sunday").click()

## 2) Select all the checkboxes
# Approach 1: Loop through checkboxes by index
# for i in range(1, 8):
#     driver.find_element(By.XPATH, f"//*[@id='post-body-1307673142697428135']/div[4]/div[{str(i)}]/input").click()

# Approach 2: Loop through checkboxes using a list of elements
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
for check in checkboxes:
    check.click()

## 3) Select multiple checkboxes by choice
# Approach 1: Loop through checkboxes by index and select specific ones
# for i in range(len(checkboxes)):
#     if i == 0 or i == 6:
#         checkboxes[i].click()

# Approach 2: Loop through checkboxes using a list of elements and select specific ones by ID
# for check in checkboxes:
#     if check.get_attribute('id') == "sunday" or check.get_attribute('id') == "saturday":
#         check.click()

## 4) Select the last 2 checkboxes
# Approach 1: Loop through the last 2 checkboxes and select them
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()

## 5) Select the first 2 checkboxes
# Approach 1: Loop through the first 2 checkboxes and select them
# for i in range(len(checkboxes) - 5):
#     checkboxes[i].click()

## 6) Clear all the checkboxes
# Loop through checkboxes and uncheck them if they are already selected
for check in checkboxes:
    if check.is_selected():
        check.click()

# Sleep for 100 seconds (not recommended, just for demonstration)
sleep(100)

# Close the browser window
driver.close()
