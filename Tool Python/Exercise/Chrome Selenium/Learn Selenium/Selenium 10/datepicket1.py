# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import datetime

# Define a class named Datepicket
class Datepicket:
    # Constructor for the Datepicket class
    def __init__(self):
        # Set up the Chrome WebDriver
        self.service = Service(executable_path="D:/Learn Python/Tool Python/Exercise/Chrome Selenium/chromedriver.exe")
        self.driver = Chrome(service=self.service)
        self.driver.maximize_window()

    # Method to get the current date
    def getdate(self):
        # Get the current date and split it into year, month, and day
        self.checkdate = datetime.datetime.now()
        self.checkdate = str(self.checkdate).split(" ")
        self.checkdate = self.checkdate[0].split("-")
        self.list_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.year = self.checkdate[0]
        self.month = self.checkdate[1]
        self.day = self.checkdate[2]

    # Method to run the date picker automation
    def run(self):
        # Navigate to a webpage with a date picker
        self.driver.get("https://jqueryui.com/datepicker/")
        self.driver.switch_to.frame(0)

        # Click on the date input field
        self.driver.find_element(By.ID, "datepicker").click()

        # Prompt the user to input the desired year, month, and day
        self.yy = str(input("Input Year: "))
        self.mm = str(input("Input Month: "))
        self.dd = str(input("Input Day: "))

        # Convert the month input to its corresponding index in the list of months
        for i in range(len(self.list_month)):
            if self.mm == self.list_month[i]:
                self.imm = i
                break

        # Loop to set the date in the date picker
        while True:
            if int(self.yy) > int(self.year):
                # Click the next month button until the desired year is reached
                self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
                if self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text == self.yy and self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text == self.mm:
                    # Select the desired day
                    d = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
                    for i in d:
                        if self.dd == i.text:
                            i.click()
                            break
                    break

            if int(self.yy) < int(self.year):
                # Click the previous month button until the desired year is reached
                self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()
                if self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text == self.yy and self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text == self.mm:
                    # Select the desired day
                    d = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
                    for i in d:
                        if self.dd == i.text:
                            i.click()
                            break
                    break

            if int(self.yy) == int(self.year):
                if int(self.imm) > int(self.month) - 1:
                    # Click the next month button until the desired month is reached
                    self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
                    if self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text == self.mm:
                        # Select the desired day
                        d = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
                        for i in d:
                            if self.dd == i.text:
                                i.click()
                                break
                        break

                if int(self.imm) < int(self.month) - 1:
                    # Click the previous month button until the desired month is reached
                    self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()
                    if self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text == self.mm:
                        # Select the desired day
                        d = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
                        for i in d:
                            if self.dd == i.text:
                                i.click()
                                break
                        break

                if int(self.imm) == int(self.month) - 1:
                    if self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text == self.mm:
                        # Select the desired day
                        d = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
                        for i in d:
                            if self.dd == i.text:
                                i.click()
                                break
                        break

        # Wait for a while (100 seconds) before closing the browser
        sleep(100)
        self.driver.close()

# Create an instance of the Datepicket class
dt = Datepicket()

# Get the current date
dt.getdate()

# Run the date picker automation
dt.run()
