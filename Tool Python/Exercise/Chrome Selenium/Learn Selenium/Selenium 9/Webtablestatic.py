# Import necessary libraries from Selenium and time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create a class for working with a web table
class Webtable_static:
    def setup(self):
        # Initialize the Chrome driver and maximize the window
        self.service = Service(executable_path="D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe")
        self.driver = Chrome(service=self.service)
        self.driver.maximize_window()

    def ws(self):
        # Navigate to a specific website
        self.driver.get("https://testautomationpractice.blogspot.com/")
        
        # 1) Count number of rows & columns
        c_row = self.driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr")
        c_col = self.driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")
        print("Number of Rows:", len(c_row))
        print("Number of Columns:", len(c_col))

        # 2) Read specific row & column data
        S_data = self.driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[4]/td[2]")
        print("Specific Data:", S_data.text)

        # 3) Read all the rows & column data
        for i in range(1, len(c_row) + 1):
            for j in range(1, len(c_col) + 1):
                if i == 1:
                    # For the header row, print column headers
                    print(self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/th[{j}]").text, end="\t\t\t")
                else:
                    # For data rows, print the data in each cell
                    print(self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[{j}]").text, end="\t\t\t")
            print()

        # 4) Read data based on condition (List book names whose author is Mukesh)
        for i in range(1, len(c_row) + 1):
            for j in range(1, len(c_col) + 1):
                if i == 1:
                    # Check if the header matches "Mukesh" and print the corresponding data
                    if self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/th[{j}]").text == "Mukesh":
                        print(f"Row {i} : Column {j} :", self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/th[{j}]").text, end="\t\t\t")
                else:
                    # Check if the cell data matches "Mukesh" and print the corresponding data
                    if self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[{j}]").text == "Mukesh":
                        print(f"Row {i} : Column {j} :", self.driver.find_element(By.XPATH, f"//*[@id='HTML1']/div[1]/table/tbody/tr[{i}]/td[{j}]").text, end="\t\t\t")
            print()

        # Wait for 100 seconds (simulating some action on the website)
        sleep(100)

        # Close the Chrome driver
        self.driver.close()

# Create an instance of the Webtable_static class
w = Webtable_static()

# Call the setup method to configure the Chrome driver
w.setup()

# Call the ws method to interact with the web table on the website
w.ws()
