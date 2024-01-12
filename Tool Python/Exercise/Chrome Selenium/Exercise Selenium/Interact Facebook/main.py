from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import re

class SET_UP:
    def __init__(self,url = "",i =0):
        self.i = i
        self.options = Options()
        self.options.add_argument(f"--user-data-dir=D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account {self.i}")
        self.driver = Chrome(options=self.options)
        self.driver.implicitly_wait(10)
        self.url = url
        self.driver.get(url)
    def close(self):
        sleep(100)
        self.driver.close()

class ACCOUNT(SET_UP):
    def __init__(self,account ,password, url="", i=0):
        self.account = account
        self.password = password
        super().__init__(url, i)
    
    def list_account(self):
        with open("account.txt","r") as ac_r:
            read = ac_r.read()
            ac_r.close()
        r_a = re.compile(r"(.*?)\|")
        r_p = re.compile(r"\|(.*?\w+)")
        self.account = r_a.findall(read)
        self.password = r_p.findall(read)
    
    def add_account(self):
        with open("account.txt","+a") as ac_w:
            acc_new = str(input("Nhap account: "))
            pass_new = str(input("Nhap password: "))
            ac_w.write("\n"+acc_new + "|" + pass_new)
            ac_w.close()
            
        
class LOGIN(ACCOUNT):
    def __init__(self, account=[], password=[], url="", i=0):
        super().__init__(account, password, url, i)

    def log(self):
        try:
            self.driver.find_element(By.XPATH,"//*[@id='m_login_email']").send_keys(self.account)
            self.driver.find_element(By.XPATH,"//*[@id='password_input_with_placeholder']/input").send_keys(self.password)
            self.driver.find_element(By.XPATH,"//*[@id='login_form']/ul/li[3]/input").click()
            if self.driver.title == "Log in to Facebook | Facebook":
                print("Login failed!!!")
            else:
                print("Success!!!")
            
        except:
            print("Error!!!")

class INTERACT(LOGIN):
    def __init__(self,target="", account=[], password=[], url="", i=0):
        self.target = target
        super().__init__(account, password, url, i)
        super().log()
    
    def like(self):
        self.driver.find_element(By.XPATH,"//*[@id='actions_2075724856126589']/table/tbody/tr/td[1]/a").click()
        atribute_aria = self.driver.find_element(By.XPATH,"//*[@id='actions_2075724856126589']/table/tbody/tr/td[1]/a").get_attribute("aria-pressed")
        if atribute_aria == "true":
            print("Like Success!!!")
        else:
            print("Like Failed!!!")
            
    def comment(self,content):
        self.driver.find_element(By.XPATH,"//*[@id='actions_2075724856126589']/table/tbody/tr/td[2]/a/span").click()
        self.driver.find_element(By.XPATH,"//*[@id='root']/section/form/div[1]/textarea").send_keys(content)
        if self.driver.title == "Comment":
            print("Comment Success!!!")
        else:
            print("Comment Failed!!!")
        
        
        
class Manage:
    def __init__(self,n = 0) -> None:
        self.n = n
    def main(self):
        pass
            

            

        
        
        

        