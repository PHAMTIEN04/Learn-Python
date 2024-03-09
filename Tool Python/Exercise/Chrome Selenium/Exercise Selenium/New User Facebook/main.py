from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
# D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account 0

options = Options()
options.add_argument(f"--user-data-dir=D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account 0")
options.add_argument('--disable-notifications')
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div /div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[2]/ div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
# //*[@id="mount_0_0_6Y"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span[1]/span/a
driver = Chrome(options=options)
driver.get("https://www.facebook.com/groups/146473906768401/members")
x_path = str(input("Input XPATH: "))
x_path = list(x_path)
x_new = ""
for i in range(2,11):
    
    for j in x_path:
        x_new+=j
    
    f = driver.find_element(By.XPATH,x_new.replace('"',"'"))
    text = str(f.get_attribute("href"))
    reg = re.compile(r"user\/(.*?)\/")
    ret = reg.findall(text)
    print(ret[0])
    x_new = ""
    x_path[168] = str(i)



sleep(100)
driver.close()
