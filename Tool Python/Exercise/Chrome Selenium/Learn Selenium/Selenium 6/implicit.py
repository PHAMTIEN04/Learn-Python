# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Set an implicit wait time of 10 seconds, which allows Selenium to wait for elements to appear
driver.implicitly_wait(10)

# Navigate to the Google website
driver.get("https://www.google.com/")

# Find an element by class name "gFyf"
find = driver.find_element(By.CLASS_NAME, "gFyf")

# Input the text "Selenium" into the found element and simulate pressing the Enter key
find.send_keys("Selenium", Keys.ENTER)

# Sleep for 10 seconds to give time for search results to load (not recommended, just for demonstration)
sleep(10)

# Close the browser window
driver.close()
