# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())

# Navigate to a specific URL using the Chrome driver
driver.get("https://money.rediff.com/index.html")

# Find and click on an element on the web page
driver.find_element(By.XPATH, "//*[@id='hm_right_container']/div[3]/div/a/div[1]/img").click()

# Pause the script for 10 seconds (useful for manual inspection or testing)
sleep(10)

# Close the current browser window/tab, but keep the driver instance open
# driver.close()

# Quit the driver, closing all associated browser windows/tabs and ending the WebDriver session
driver.quit()
