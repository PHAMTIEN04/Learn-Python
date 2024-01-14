import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
# with open("account.txt","r") as ac_r:
#     read = ac_r.read()

#     r_a = re.compile(r"(.*?)\|")
#     r_p = re.compile(r"\|(.*?\w+)")
#     account = r_a.findall(read)
#     password = r_p.findall(read)
    
#     print("Account :",account)
#     print("Password :",password)
# with open("account.txt","+a") as ac_w:
#     acc_new = str(input("Nhap account: "))
#     pass_new = str(input("Nhap password: "))
#     write = ac_w.write("\n"+acc_new + "|" + pass_new)
#     ac_w.close()

driver = Chrome()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")

sleep(100)
driver.close()