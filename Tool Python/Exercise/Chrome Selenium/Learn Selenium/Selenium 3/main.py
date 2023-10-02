from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Set the path to the Chrome WebDriver executable
path = r"D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

# Create a Service object for the WebDriver with the specified path
service = Service(executable_path=path)

# Initialize the Chrome WebDriver with the service
driver = Chrome(service=service)

# Navigate to the website
driver.get("http://www.automationpractice.pl/index.php")

# Absolute XPath
# Find the search input field by absolute XPath and input text
driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("Tiendeptrai")
# Find the search button by absolute XPath and click it
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative XPath
# Find the search input field by relative XPath and input text
driver.find_element(By.XPATH , "//*[@id='search_query_top']").send_keys("Tiendeptrai")
# Find the search button by relative XPath and click it
driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()

# or
# Find the search input field by using 'or' in XPath and input text
driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
# Find the search button by using 'or' in XPath and click it
driver.find_element(By.XPATH, "//button[@name='submit_search' and @class='btn btn-default button-search']").click()

# contains() & starts-with()
# Find the search input field using contains() in XPath and input text
driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys('T-shirts')
# Find the search button using starts-with() in XPath and click it
driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()

# text()
# Click on the 'Women' link by locating it with its visible text
driver.find_element(By.XPATH,"//a[text()='Women']").click()

# Wait for 100 seconds before closing the WebDriver (for demonstration purposes)
sleep(100)
driver.close()
