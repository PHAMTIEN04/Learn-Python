# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Navigate to the "https://demo.nopcommerce.com/" website
driver.get("https://demo.nopcommerce.com/")

# Maximize the browser window for a better view
driver.maximize_window()

# Find and click on a link using its text
# Uncomment the following line to click on the "Computers" link
# driver.find_element(By.LINK_TEXT, "Computers").click()

# Find the number of links on the page
links = driver.find_elements(By.CSS_SELECTOR, "a")
print("Total links found on the page:", len(links))

# Loop through all the links and print their text
for link in links:
    print(link.text)

# Sleep for 100 seconds (not recommended, just for demonstration)
sleep(100)

# Close the browser window
driver.close()
