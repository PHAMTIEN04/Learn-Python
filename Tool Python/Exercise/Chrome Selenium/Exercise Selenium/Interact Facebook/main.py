from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import re



class ACCOUNT:
    def __init__(self,account="" ,password=""):
        self.account = account
        self.password = password
    
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
    
    def len_account(self):
        self.list_account()
        if len(self.account) == len(self.password):
            return len(self.account)
        return -1

class SET_UP:
    def __init__(self,url = "https://mbasic.facebook.com/",i =0):
        self.i = i
        self.options = Options()
        self.options.add_argument(f"--user-data-dir=D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account {self.i}")
        self.driver = Chrome(options=self.options)
        self.driver.implicitly_wait(10)
        self.url = url
        self.driver.get(self.url)
        
    def get_driver(self):
        return self.driver
    def get_title(self):
        return self.driver.title
    def close(self):
        sleep(3)
        self.driver.close()          
        
class LOGIN(SET_UP,ACCOUNT):
    def __init__(self, account="",password="",url="https://mbasic.facebook.com/", i=0):
        self.account = account
        self.password = password
        super().__init__(url, i)
        self.list_account()

    def log(self):
        
        try:
            if self.get_title() == "Facebook – log in or sign up":
                self.driver.find_element(By.XPATH,"//*[@id='m_login_email']").send_keys(self.account[self.i])
                self.driver.find_element(By.XPATH,"//*[@id='password_input_with_placeholder']/input").send_keys(self.password[self.i])
                self.driver.find_element(By.XPATH,"//*[@id='login_form']/ul/li[3]/input").click()
                if self.get_title() == "Log in to Facebook | Facebook":
                    print(f"Account:{self.account[self.i]} Login failed!!!")
                else:
                    print(f"Account:{self.account[self.i]} Login Success!!!")
            
        except:
            print("Error!!!")

# a = LOGIN(url ="https://mbasic.facebook.com/")
# a.log()
class INTERACT(LOGIN):
    def __init__(self, link="", account="", password="", url="https://mbasic.facebook.com/", i=0):
        self.link = link
        super().__init__(account, password, url, i)
        self.log()

    def like(self):
        self.driver.get(self.link)
        self.driver.find_element(By.XPATH, "//*[@id='actions_2075724856126589']/table/tbody/tr/td[1]/a").click()
        atribute_aria = self.driver.find_element(By.XPATH, "//*[@id='actions_2075724856126589']/table/tbody/tr/td[1]/a").get_attribute("aria-pressed")
        if atribute_aria == "true":
            print("Like Success!!!")
        else:
            print("Like Failed!!!")

    def comment(self, content):
        content = str(input("Content: "))
        self.driver.get(self.link)
        self.driver.find_element(By.XPATH, "//*[@id='actions_2075724856126589']/table/tbody/tr/td[2]/a/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='root']/section/form/div[1]/textarea").send_keys(content)
        if self.driver.title == "Comment":
            print("Comment Success!!!")
        else:
            print("Comment Failed!!!")
        
        
        
class MANAGE:
    def main(self):
        link = str(input("Link Post :"))
        print("**INTERACT**")
        print("1.Like")
        print("2.Comment")
        print("3.All")
        choose = int(input("Choose: "))
        a = ACCOUNT()
        a.list_account()
        i = 0
        while i < a.len_account():
            try:
                mn = INTERACT(link=link, account=a.account[i], password=a.password[i], url="https://mbasic.facebook.com/", i=i)
                if mn.get_title() !=  "Facebook – log in or sign up" and mn.get_title() !=  "Log in to Facebook | Facebook":   
                    if choose == 1:
                        mn.like()
                    
                    if choose == 2:
                        mn.comment()
                    
                    if choose == 1 and choose == 2:
                        mn.like()
                        mn.comment()
                sleep(10)    
                mn.close()
                i = i + 1
                
            except:
                print("Error!!!")

a = MANAGE()
a.main()

    

            

        
        
        

        