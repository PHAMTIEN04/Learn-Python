# Import necessary modules and classes from Selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
from time import sleep

# Initialize the Chrome driver using ChromeDriverManager to handle automatic driver setup
driver = Chrome(ChromeDriverManager().install())

# Navigate to the "http://www.deadlinkcity.com/" website
driver.get("http://www.deadlinkcity.com/")

# Find all the anchor elements on the web page using CSS selector
link = driver.find_elements(By.CSS_SELECTOR, "a")

# Print the number of links found on the page
print("Total links found:", len(link))

# Loop through each link and check if it's a valid URL
for i in link:
    # Get the URL from the 'href' attribute of the anchor element
    url = i.get_attribute("href")
    
    # Send an HTTP GET request to the URL
    check = requests.get(url)
    
    # Check the response status code
    if check.status_code == 200:
        print("Status: 200 (Success)")
        print("URL Success:", url)
    else:
        print("URL Error!!!")

# Sleep for 100 seconds (not recommended, just for demonstration)
sleep(100)

# Close the browser window
driver.close()
