# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Create a WebDriverWait instance with a timeout of 10 seconds
my_wait = WebDriverWait(driver, 10)

# Navigate to the Google website
driver.get("https://www.google.com/")

# Find the search input element by its class name "gLFyf"
find = driver.find_element(By.CLASS_NAME, "gLFyf")

# Input the text "Selenium" into the search input and simulate pressing the Enter key
find.send_keys("Selenium", Keys.ENTER)

# Use WebDriverWait to wait for the presence of the first search result link
click_find = my_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div[1]/div/div/span/a/h3")))

# Click on the first search result link
click_find.click()

# Sleep for 100 seconds (not recommended, just for demonstration)
sleep(100)

# Close the browser window
driver.close()
