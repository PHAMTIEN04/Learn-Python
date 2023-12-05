from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class BoostrapDropDown:
    def __init__(self):
        # Initialize the Chrome WebDriver
        self.driver = Chrome(executable_path=ChromeDriverManager().install())
        
        # Set implicit wait time for the WebDriver
        self.driver.implicitly_wait(10)
        
        # Maximize the browser window
        self.driver.maximize_window()
        
        # Open the specified URL
        self.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
        
    def run(self):
        # Click on the dropdown to open the country selection
        self.driver.find_element(By.XPATH, "//*[@id='select2-billing_country-container']").click()
        
        # Find all the options in the dropdown
        country_options = self.driver.find_elements(By.XPATH, "/html/body/span/span/span[2]/ul/li")
        
        # Print the number of options in the dropdown
        print("Number of countries:", len(country_options))
        
        # Iterate through each option in the dropdown
        for option in country_options:
            # Check if the option text is "Vietnam"
            if option.text == "Vietnam":
                # Click on the "Vietnam" option
                option.click()
                break
        
        # Sleep to observe the selected option (you may adjust the duration)
        sleep(10)
        
        # Close the browser window
        self.driver.close()

# Create an instance of the BoostrapDropDown class
bootstrap_dropdown = BoostrapDropDown()

# Run the automation script
bootstrap_dropdown.run()
