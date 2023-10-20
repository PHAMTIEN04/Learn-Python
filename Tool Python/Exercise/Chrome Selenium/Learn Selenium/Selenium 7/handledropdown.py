# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Set an implicit wait time of 30 seconds to wait for elements to appear
driver.implicitly_wait(30)

# Navigate to the OpenCart registration page
driver.get("https://www.opencart.com/index.php?route=account/register")

# Find the dropdown element by its XPath
dropd = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# Select options from the dropdown using various methods
# dropd.select_by_visible_text("QA Engineer")
# dropd.select_by_index(1)
# dropd.select_by_value("2")

# Capture all the options in the dropdown and print their count
alloptions = dropd.options
print("Total options in the dropdown:", len(alloptions))

# Uncomment the following lines to print the text of each option
# for opt in alloptions:
#    print(opt.text)

# Select an option from the dropdown without using the built-in method
# Uncomment the following lines to select an option by its text (e.g., "India")
# for opt in alloptions:
#     if opt.text == "India":
#         opt.click()
#         break

# Find the options using a different XPath and print their count
alloptions = driver.find_element(By.XPATH, "//*[@id='input-country']/option")
print("Total options using a different XPath:", len(alloptions))

# Sleep for 100 seconds (not recommended, just for demonstration)
sleep(100)

# Close the browser window
driver.close()
