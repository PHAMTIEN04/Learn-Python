# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())
# Navigate to a specific URL using the Chrome driver
driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")

# Find the element with the specified XPath that represents the header on the registration page
check_a = driver.find_element(By.XPATH, "//*[@id='content']/h1")

# Check if the element is displayed on the page
print("Display Status: ", check_a.is_displayed())

# Check if the element is enabled (typically used for form elements)
print("Enabled Status: ", check_a.is_enabled())

# Find the "No" and "Yes" radio buttons for the newsletter subscription
check_no = driver.find_element(By.XPATH, "//*[@id='input-newsletter-no']")
check_yes = driver.find_element(By.XPATH, "//*[@id='input-newsletter-yes']")

# Check if the "No" radio button is selected
print("Selected No Status: ", check_no.is_selected())

# Check if the "Yes" radio button is selected
print("Selected Yes Status: ", check_yes.is_selected())

# Click on the "Yes" radio button
check_yes.click()

# After clicking, check if the "No" radio button is selected (it should be unselected)
print("Selected No Status: ", check_no.is_selected())

# Check if the "Yes" radio button is selected (it should be selected)
print("Selected Yes Status: ", check_yes.is_selected())

# Pause the script for 10 seconds (useful for manual inspection or testing)
sleep(10)

# Close the Chrome driver, terminating the browser session
driver.close()
