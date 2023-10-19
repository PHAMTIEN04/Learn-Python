# Import necessary libraries from Selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = Chrome(ChromeDriverManager().install())
# Navigate to a website
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# Use various XPath axes to locate elements and perform actions

# Find a descendant element (any element nested within the ancestor <tr> element)
test_descendant = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr/descendant::*").text
print(test_descendant)

# Find an ancestor element (<tr> element) of the <a> element
test_ancestor = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr").text
print(test_ancestor)

# Find the parent element (<td> element) of the <a> element
test_parent = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/parent::td").text
print(test_parent)

# Find the <a> element itself
test_self = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/self::a").text
print(test_self)

# Find a child element (<td> element) within the ancestor <tr> element
test_child = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr/child::td").text
print(test_child)

# Find all following elements of the <a> element
test_following = driver.find_elements(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/following::*")
print(len(test_following))

# Find all following sibling elements of the ancestor <tr> element
test_following_sibling = driver.find_elements(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr/following-sibling::*")
print(len(test_following_sibling))

# Find a preceding element (<td> element) before the ancestor <tr> element
test_preceding = driver.find_element(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr/preceding::td").text
print(test_preceding)

# Find all preceding sibling elements of the ancestor <tr> element
test_preceding_sibling = driver.find_elements(By.XPATH, "//a[contains(normalize-space(.),'Indian Energy Exchan')]/ancestor::tr/preceding-sibling::*")
print(len(test_preceding_sibling))

# Add a sleep to keep the browser window open for a while (100 seconds)
sleep(100)

# Close the WebDriver session
driver.close()


## TEST
# from selenium import webdriver 
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from time import sleep

# path = r"D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe"

# service = Service(executable_path=path)


# driver = Chrome(service=service)

# driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# select = driver.find_elements(By.CSS_SELECTOR, 'td')
# cnt = 1
# print(len(select))
# for i in select:
#     if i.text == "Stocks":
        
#         break
#     print(i.text,end=" ")
#     cnt = cnt + 1
#     if cnt == 6:
#         print()
#         cnt = 1
        




# sleep(100)
# driver.close()