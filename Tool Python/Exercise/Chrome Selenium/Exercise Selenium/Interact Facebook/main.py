from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from time import sleep
import re
import os



class ACCOUNT:
    def __init__(self,account="" ,password=""):
        self.account = account
        self.password = password
    
    def list_account(self):
        with open("account.txt","r") as ac_r:
            read = ac_r.read()
            ac_r.close()
        r_a = re.compile(r"(.*?)\|")
        r_p = re.compile(r"\|(.*)")
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
        location = os.getcwd()
        self.options.add_argument(f"--user-data-dir={location}\Facebook account\Account {self.i}")
        self.options.add_argument('--disable-notifications')
        # self.options.add_argument("--headless")
        self.options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
            )
        self.driver = Chrome(options=self.options)
        self.driver.set_window_size(500,500)
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
                self.driver.find_element(By.CLASS_NAME,"inputtext._55r1._6luy").send_keys(self.account[self.i])
                self.driver.find_element(By.CLASS_NAME,"inputtext._55r1._6luy._9npi").send_keys(self.password[self.i])
                # sleep(3)
                self.driver.find_element(By.CLASS_NAME,"_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()
                if self.get_title() != "Facebook – log in or sign up" and self.get_title() != "Log in to Facebook":
                    print(f"Account:{self.account[self.i]} Login Success!!!")
                else:
                    print(f"Account:{self.account[self.i]} Login failed!!!")
            
        except Exception as e:
            print("Error:",e)

# a = LOGIN(url ="https://www.facebook.com/")
# a.log()
class INTERACT(LOGIN):
    def __init__(self, link="", account="", password="", url="https://www.facebook.com/", i=0):
        self.link = link
        super().__init__(account, password, url, i)
        self.log()

    def like(self):
        self.driver.get(self.link)
        
        if self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Like" or self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Thích":
            # sleep(3)
            self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").click()

    def check_like(self):
        if self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Remove Like" or self.driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3").get_attribute("aria-label") == "Gỡ Thích":
            return "Success!!!"
        else:
            return "Failed!!!"
    def comment(self):
        with open("content.txt","r",encoding="utf-8") as r_content:
            read = r_content.read()
            list_r = read.split("\n")
            r_content.close()
        content = random.choice(list_r)
        self.driver.get(self.link)
        self.driver.find_element(By.CLASS_NAME, "xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.notranslate").send_keys(content,Keys.ENTER)
        # self.driver.find_element(By.XPATH, "//*[@id='root']/section/form/div[1]/textarea").send_keys(content)

            
    def check_cmt(self):
        check_comment = self.driver.find_element(By.CLASS_NAME,"xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs")

        if check_comment:
            return "Success!!!"
        else:
            return "Failed!!!"
class INTERFACE:
    check = False
    def __init__(self):
        self.win = Tk()
        self.win.geometry("700x500")
        self.win.resizable(False,False)
        self.win.title("Interact Facebook")
        self.win.iconbitmap("./iconfb.ico")
        self.treeview = ttk.Treeview(self.win)
    def treeview_set(self,i,id,type,status):
        self.treeview.insert(parent="", index="end", iid=i, text=i, values=(id,type,status))
        self.treeview.update()
    def resize_img(self,path,width,height): # Function Resize Image
        img = Image.open(path)
        img = img.resize((width,height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    def ilike(self):
        return "Like"
    
    def icmt(self):
        return "Comment"   
    
    def iall(self):
        return "All"
    
    def Build(self):
        self.treeview.configure(height=20)
        self.treeview['columns'] = ("ID","Type","Status")

        self.treeview.column("#0",width=50,anchor=W)
        self.treeview.column("ID",anchor=CENTER,width=150)
        self.treeview.column("Type",anchor=CENTER,width=70)
        self.treeview.column("Status",anchor=CENTER,width=70)

        self.treeview.heading("#0",text="STT",anchor=CENTER)
        self.treeview.heading("ID",text="ID",anchor=CENTER)
        self.treeview.heading("Type",text="Type",anchor=CENTER)
        self.treeview.heading("Status",text="Status",anchor=CENTER)
    
        

        self.treeview.place(relx=0.085,rely=0.08)

        link_text = Label(self.win,text="Get Link",font=("Arial",10,"bold"))
        link_text.place(relx=0,rely=0.02)

        self.Link_entry = Entry(self.win,width=55)
        self.Link_entry.place(relx=0.09,rely=0.025)

        
class MANAGE(INTERFACE):
    def __init__(self):
        super().__init__()
        super().Build()

    def m_type(self):
        if self.ilike():
            return self.ilike()
        if self.icmt():
            return self.icmt()
        if self.iall():
            return self.iall()

    def perform_like(self):
        link = self.Link_entry.get()
        self.interact(link, "Like")
        self.Link_entry.delete(0,END)

    def perform_comment(self):
        link = self.Link_entry.get()
        self.interact(link, "Comment")
        self.Link_entry.delete(0,END)

    def perform_all(self):
        link = self.Link_entry.get()
        self.interact(link, "All")
        self.Link_entry.delete(0,END)

    def interact(self, link, action_type):
        a = ACCOUNT()
        a.list_account()
        i = 0
        while i < a.len_account():
            try:
                mn = INTERACT(link=link, account=a.account[i], password=a.password[i], url="https://www.facebook.com/", i=i)
                
                if mn.get_title() != "Facebook – log in or sign up" and mn.get_title() != "Log in to Facebook":
                    if action_type == "Like":
                        mn.like()
                        self.treeview_set(i, a.account[i], "Like", mn.check_like())

                    if action_type == "Comment":
                        mn.comment()
                        self.treeview_set(i, a.account[i], "Comment", mn.check_cmt())

                    if action_type == "All":
                        mn.like()
                        mn.comment()
                        if mn.check_like() == "Success!!!" and mn.check_cmt() == "Success!!!":
                            self.treeview_set(i, a.account[i], "All", "Success!!!")
                        else:
                            self.treeview_set(i, a.account[i], "All", "Faild!!!")

                mn.close()
                i = i + 1

            except Exception as e:
                print(f"Error: {e}")
                i = i + 1

    def main(self):
        rz_img = self.resize_img(f"D:/Learn Python/Tool Python/Exercise/Chrome Selenium/Exercise Selenium/Interact Facebook/add.png",215,160)
        lb_img = Label(self.win,text = "aaa",image=rz_img)
        
        lb_img.place(relx =0.65,rely=0.01)
        like_button = Button(self.win, text="Like", width=30, height=5, border=5, command=self.perform_like)
        like_button.place(relx=0.65, rely=0.35)

        cmt_button = Button(self.win, text="Comment", width=30, height=5, border=5, command=self.perform_comment)
        cmt_button.place(relx=0.65, rely=0.55)

        all_button = Button(self.win, text="All", width=30, height=5, border=5, command=self.perform_all)
        all_button.place(relx=0.65, rely=0.75)

        
        self.win.mainloop()


mn = MANAGE()
mn.main()

        
        
        

        