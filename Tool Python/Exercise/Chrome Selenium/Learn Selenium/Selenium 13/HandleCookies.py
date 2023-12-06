from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class HandleCookies:
    def __init__(self):
        # Initialize the Chrome web driver using the ChromeDriverManager to manage the driver version
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        
        # Set an implicit wait time of 10 seconds for the WebDriver
        self.driver.implicitly_wait(10)
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Navigate to the desired website
        self.driver.get("https://coder.husc.edu.vn/")
    
    def get_cookies(self):
        # Get and print the cookies present in the browser
        cookies = self.driver.get_cookies()
        print("Length Cookies:", len(cookies))
        for c in cookies:
            print("Cookies:", c)
            
    def add_cookies(self):
        # Add cookies to the browser
        self.driver.add_cookie({"name": "csrftoken", "value": "8KjHZn90Gyoh7d2IMu0l2JHrdVZVh0buUkKyrgV2aIu2cLZXCObtUNAI6vd5Cc9B"})
        self.driver.add_cookie({"name":"sessionid","value":"z0heiz4i7z22bgd5man7iapm1qlzi6n8"})
        
        # Refresh the page to apply the added cookies
        self.driver.refresh()
    
    def delete_cookie(self, cookie_name):
        # Delete a specific cookie by name
        self.driver.delete_cookie(cookie_name)
    
    def delete_all_cookies(self):
        # Delete all cookies in the browser
        self.driver.delete_all_cookies()
    
    def close(self):
        # Pause the script for 100 seconds (for demonstration purposes, you may adjust this)
        sleep(100)
        
        # Close the browser window
        self.driver.close()

# Create an instance of the HandleCookies class
h = HandleCookies()

# Get and print initial cookies
h.get_cookies()

# Add cookies and refresh the page
h.add_cookies()

# Get and print cookies after adding
h.get_cookies()

# Delete a specific cookie (you may adjust the cookie name)
h.delete_cookie("csrftoken")

# Get and print cookies after deletion
h.get_cookies()

# Delete all cookies
h.delete_all_cookies()

# Get and print cookies after deleting all
h.get_cookies()

# Close the browser
h.close()
