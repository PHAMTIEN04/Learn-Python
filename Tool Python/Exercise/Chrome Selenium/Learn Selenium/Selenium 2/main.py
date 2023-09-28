# Import necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Import the sleep function from the time module
from time import sleep

# Specify the path to the Chrome WebDriver executable
path = "D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

# Create a service object for the WebDriver with the specified path
service = Service(executable_path=path)

# Create a Chrome WebDriver instance using the service
driver = webdriver.Chrome(service=service)

# Open the Facebook website
driver.get("https://www.facebook.com/")

## Various methods to locate and interact with web elements on the page

# ID:
# Locate the element with the "email" ID and send keys (input text) to it
# driver.find_element(By.ID, "email").send_keys("abc@")

# Name:
# Locate the element with the "email" name attribute and send keys to it
# driver.find_element(By.NAME, "email").send_keys("Tiendeptrai")

# Link Text:
# Locate and click an element with the exact link text "Create a Page"
# driver.find_element(By.LINK_TEXT, "Create a Page").click()

# Partial Link Text:
# Locate and click an element with a partial link text "Create"
# driver.find_element(By.PARTIAL_LINK_TEXT, "Create").click()

# Class Name:
# Locate an element with the class name "signupclass" and click it
# driver.find_element(By.CLASS_NAME, "signupclass").click()

# Tag Name:
# Locate all 'a' elements on the page and print the number of elements found
# l = driver.find_elements(By.TAG_NAME, "a")
# print(len(l))

### CSS Selectors:

# Tag ID:
# Locate an 'input' element with the ID "email" and send keys to it
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@")

# Tag Class:
# Locate an 'input' element with the class "inputtext" and send keys to it
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@")

# Tag Attribute:
# Locate an 'input' element with a "data-testid" attribute of "royal_email" and send keys to it
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal_email"]').send_keys("@abc")

# Tag Class and Attribute:
# Locate an 'input' element with both class "inputtext" and "data-testid" attribute "royal_email" and send keys to it
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid="royal_email"]').send_keys("@abc")

# Pause execution for 100 seconds (for demonstration purposes)
sleep(100)

# Close the WebDriver instance
driver.close()
