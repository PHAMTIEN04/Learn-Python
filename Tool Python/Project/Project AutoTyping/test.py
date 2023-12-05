# Import necessary modules from the Selenium package.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from threading import Thread
from time import sleep
def open():
    i = 0
    x = 0
    y = 0
    while True:
    # Configure Chrome options to disable loading images.
        options = webdriver.ChromeOptions()
        prefs = {
        "profile.managed_default_content_settings.images": 2
    
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        # options.add_argument("--window-size=600,600")  
        # options.add_argument(f"--window-position={x},{y}")  # Đặt vị trí của cửa sổ trình duyệt



# Set the path to the ChromeDriver executable based on your installation location.
        driver_path = "D:/Learn Python/Tool Python/Project AutoTyping/chromedriver"

# Create a Service object for ChromeDriver.
        service = Service(executable_path=driver_path)

# Initialize the WebDriver with configured options and service.
        driver = webdriver.Chrome(service=service, options=options)

# Navigate to the target website.
        driver.get("https://baicasinhvien.hoisinhvien.com.vn/videos/KV3222")


    
        driver.quit()
        i = i + 1
        x = x + 1 
        y = y + 1
        print("View : +",i,sep="")
        
        
target = 10
t_l = []
for i in range(target):
    thread = Thread(target=open)
    t_l.append(thread)
    
for thread in t_l:
    thread.start()
    
for thread in t_l:
    thread.join()
    