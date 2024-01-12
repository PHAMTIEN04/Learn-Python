# Import necessary modules from the Selenium package.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Configure Chrome options to disable loading images.
options = webdriver.ChromeOptions()
prefs = {
    "profile.managed_default_content_settings.images": 2
}
options.add_experimental_option("prefs", prefs)

# Set the path to the ChromeDriver executable based on your installation location.
driver_path = "D:/Learn Python/Tool Python/Project AutoTyping/chromedriver"

# Create a Service object for ChromeDriver.
service = Service(executable_path=ChromeDriverManager().install())

# Initialize the WebDriver with configured options and service.
driver = webdriver.Chrome(service=service,options=options)

# Navigate to the target website.
driver.get("https://10fastfingers.com/competition/659d89da5e61a")

# Wait for the page to load completely.
sleep(5)

# Dismiss any cookie consent dialogs by clicking the second button.
js_click = "document.querySelectorAll('.CybotCookiebotDialogBodyButton')[1].click()"
driver.execute_script(js_click)

# Wait for an element with ID 'row1' to be present on the page.
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'row1')))



# Find the div element with ID 'row1'.
div_element = driver.find_element(By.ID, 'row1')

# Find all span elements within the div element.
span_elements = div_element.find_elements(By.CSS_SELECTOR, 'span')

# Loop through the list of span elements and print their text content.
for span_element in range(len(span_elements)):
    print("Content of a span element:", span_elements[span_element].text)

    # Find the input field by ID 'inputfield' and type the text content of the span element followed by a space.
    input_field = driver.find_element(By.ID, 'inputfield')
    input_field.send_keys(span_elements[span_element].text)
    sleep(0.01)
    input_field.send_keys(" ")
    sleep(0.01)

    # Check if the next span element is empty (end of content), and exit the loop if it is.
    if span_elements[span_element + 1].text == "":
        break

# Wait for a longer duration (200 seconds) to keep the browser window open.
sleep(200)
driver.quit()