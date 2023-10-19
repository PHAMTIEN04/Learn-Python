# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())
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
