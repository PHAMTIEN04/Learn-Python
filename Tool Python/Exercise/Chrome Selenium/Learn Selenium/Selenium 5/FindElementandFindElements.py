# Import necessary modules from the Selenium library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())

# Navigate to a specific URL using the Chrome driver
driver.get("https://money.rediff.com/gainers")

# Find a single element on the page using its XPath and print its text
finde = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[1]/td[1]/a")
print("Text of the found element: ", finde.text)

# Find multiple elements on the page using their XPath
findes = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr")

# Print the number of elements found
print("Number of elements found: ", len(findes))

# Print the text of the first element found
print("Text of the first element: ", findes[0].text)

# Loop through all found elements and print their text
for t in findes:
    print(t.text)

# Pause the script for 10 seconds (useful for manual inspection or testing)
sleep(10)

# Close the Chrome driver, terminating the browser session
driver.close()
