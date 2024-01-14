from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    def __init__(self,url = "https://www.facebook.com/",i =0):
        self.i = i
        self.options = Options()
        self.options.add_argument(f"--user-data-dir=D:\Learn Python\Tool Python\Exercise\Chrome Selenium\Exercise Selenium\Interact Facebook\Facebook account\Account {self.i}")
        self.options.add_argument('--disable-notifications')
        self.options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
            )
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
    def __init__(self, account="",password="",url="https://www.facebook.com/", i=0):
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
                if self.get_title() != "Facebook – log in or sign up" and self.get_title() != "Log in to Facebook":
                    print(f"Account:{self.account[self.i]} Login Success!!!")
                else:
                    print(f"Account:{self.account[self.i]} Login failed!!!")
            
        except:
            print("Error!!!")

# a = LOGIN(url ="https://www.facebook.com/")
# a.log()
class INTERACT(LOGIN):
    def __init__(self, link="", account="", password="", url="https://www.facebook.com/", i=0):
        self.link = link
        super().__init__(account, password, url, i)
        self.log()

    def like(self):
        self.driver.get(self.link)
        
        if self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Like":
            self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").click()
        if self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Remove Like":
            print("Like Success!!!")
        else:
            print("Like Failed!!!")

    def comment(self):
        content = str(input("Content: "))
        self.driver.get(self.link)
        self.driver.find_element(By.CLASS_NAME, "xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.notranslate").send_keys(content,Keys.ENTER)
        # self.driver.find_element(By.XPATH, "//*[@id='root']/section/form/div[1]/textarea").send_keys(content)
        check_comment = self.driver.find_element(By.CLASS_NAME,"xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs")

        if check_comment:
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
                mn = INTERACT(link=link, account=a.account[i], password=a.password[i], url="https://www.facebook.com/", i=i)
                if mn.get_title() !=  "Facebook – log in or sign up" and mn.get_title() !=  "Log in to Facebook":   
                    if choose == 1:
                        mn.like()

                    if choose == 2:
                        mn.comment()

                    
                    if choose == 1 and choose == 2:
                        mn.like()
                        mn.comment()

                mn.close()
                i = i + 1
                
                
                
            except:
                print("Error!!!")
                i = i + 1

a = MANAGE()
a.main()

    

            

        
        
        

        