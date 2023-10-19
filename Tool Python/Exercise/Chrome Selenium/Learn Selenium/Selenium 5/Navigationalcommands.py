# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())
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
