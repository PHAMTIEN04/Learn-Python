# Import necessary modules and classes from the Selenium package
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from time import sleep

# Create a class for working with a dynamic web table
class Webtable_Dynamic:
    def setup(self):
        # Specify the path to the Chrome WebDriver executable
        self.service = Service(executable_path="D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe")
        # Create a Chrome driver with the specified service
        self.driver = Chrome(service=self.service)

    def wd(self):
        # Maximize the browser window
        self.driver.maximize_window()
        # Set an implicit wait to 30 seconds to allow elements to load
        self.driver.implicitly_wait(30)
        # Navigate to the login page of the website
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Locate and fill in the username field
        account_log = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        account_log.send_keys("Admin")

        # Locate and fill in the password field
        password_log = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/1/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        password_log.send_keys("admin123")

        # Locate and click the login button
        login = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        login.click()

        # Locate and click the "Admin" menu
        click_admin = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
        click_admin.click()

        # Find a list of switch elements within the admin panel
        switch = self.driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[4]/nav/ul/li")
        sum_row = 0
        check = 1

        # Iterate through the switch elements
        for sw in switch:
            try:
                if sw.text != '':
                    # Click on the switch element
                    sw.click()

                    # Find all rows within the table
                    rows_number = self.driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div")

                    # Iterate through the rows and retrieve data
                    while check <= len(rows_number):
                        data = self.driver.find_element(By.XPATH, f"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[{check}]/div/div[2]")
                        print("Username:", data.text)
                        check = check + 1
                    check = 1
                    print("Switch:", sw.text)
                    print("Rows Number:", len(rows_number))
                    sum_row = sum_row + len(rows_number)
            except:
                pass

        # Print the total number of rows
        print("Total Rows Number:", sum_row)

        # Find all column elements within the table
        cols_number = self.driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div")

        # Print the total number of columns
        print("Cols Number:", len(cols_number))

        # Add a sleep statement to keep the browser open for 100 seconds (you may adjust this as needed)
        sleep(100)

        # Close the browser window
        self.driver.close()

# Create an instance of the Webtable_Dynamic class
w = Webtable_Dynamic()

# Call the setup method to initialize the WebDriver and open the webpage
w.setup()

# Call the wd method to perform the web scraping and data extraction
w.wd()
